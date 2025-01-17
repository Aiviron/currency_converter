# Currency Converter

Currency Converter is a web application that allows users to convert currencies using an API to fetch the latest exchange rates.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [License](#license)

## Description

Currency Converter provides a user interface for selecting currencies and entering an amount to convert. The application uses FastAPI to create the backend API and HTML/JavaScript for the frontend.

## Installation

To install and run the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/Aiviron/currency_converter.git
    cd currency_converter
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set the `API_KEY` environment variable with your API key from [exchangerate-api](https://www.exchangerate-api.com/):
    ```sh
    export API_KEY=your_api_key
    ```

4. Start the server:
    ```sh
    uvicorn main:app --reload
    ```

## Usage

1. Open your browser and go to `http://127.0.0.1:8000`.
2. Select the currencies to convert from the dropdown menus.
3. Enter the amount to convert.
4. Click the "Convert" button to perform the conversion.

## API

### Get Available Currencies

**URL:** `/currencies`

**Method:** `GET`

**Description:** Returns a list of available currencies.

**Example Response:**
```json
{
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    ...
}
