from pydantic import BaseModel

class ConversionRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: float

class ConversionResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    converted_amount: float
    rate: float
