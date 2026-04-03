# Binance Futures Trading Bot (Testnet)

## Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI-based input
- Logging of API requests and responses
- Error handling

## Setup

1. Install dependencies:
pip install -r requirements.txt

2. Add API keys in .env:
API_KEY=your_key
API_SECRET=your_secret

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000

## Logs
Check bot.log for request and response logs