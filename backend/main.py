from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from schemas import ConversionRequest, ConversionResponse
from os import environ

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = environ.get("API_KEY")
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

@app.post("/convert", response_model=ConversionResponse)
async def convert_currency(conversion_request: ConversionRequest):
    from_currency = conversion_request.from_currency
    to_currency = conversion_request.to_currency
    amount = conversion_request.amount

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}{from_currency}")
            response.raise_for_status()
            data = response.json()

            if to_currency not in data["conversion_rates"]:
                raise HTTPException(status_code=404, detail="Currency not found")

            rate = data["conversion_rates"][to_currency]
            converted_amount = rate * amount

            return ConversionResponse(
                from_currency=from_currency,
                to_currency=to_currency,
                amount=amount,
                converted_amount=converted_amount,
                rate=rate
            )
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/currencies")
async def get_currencies():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}USD")
            response.raise_for_status()
            data = response.json()
            return data["conversion_rates"]
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

