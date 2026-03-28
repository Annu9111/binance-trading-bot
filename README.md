# Binance Futures Testnet Trading Bot

## Overview
This project is a simplified trading bot that interacts with Binance Futures Testnet (USDT-M).  
It allows users to place MARKET and LIMIT orders using a command-line interface (CLI).  
The project follows a clean modular structure with proper validation, logging, and error handling.

---

## Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI-based input
- Input validation (symbol, side, type, quantity, price)
- Logging of API requests, responses, and errors

---

## Setup Steps

1. Clone the repository:git clone <your-repo-link>
cd trading_bot

2. Create a virtual environment:python -m venv venv
venv\Scripts\activate

3. Install dependencies:pip install -r requirements.txt
4. Create a `.env` file in the root directory:API_KEY=api_key
API_SECRET=secret_key
BASE_URL=https://testnet.binancefuture.com

5. Generate API keys from Binance Futures Testnet:
https://testnet.binancefuture.com

---

## How to Run

### Market Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

### Limit Order Example
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 60000

---

## Output

- Successful order:Order Successful 
{orderId, status, executedQty, avgPrice}

- Logs are stored in:bot.log

---

## Project Structure
trading_bot/
│
├── bot/
│ ├── client.py # Binance API connection
│ ├── orders.py # Order logic
│ ├── validators.py # Input validation
│ ├── logging_config.py
│
├── cli.py # CLI entry point
├── requirements.txt
├── README.md


---

## Assumptions

- The user has a valid Binance Futures Testnet account
- API keys are correctly configured in `.env`
- Minimum notional value (≥ 100 USDT) is required for orders
- Internet connection is available for API calls

---

## Notes

- This project uses Binance Futures Testnet (no real money involved)
- Limit orders may remain in `NEW` status until price conditions are met
