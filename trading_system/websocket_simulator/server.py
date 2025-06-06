import asyncio
from websockets.asyncio.server import serve
import json
import random
from datetime import datetime

TICKERS = ["AAPL", "GOOG", "TSLA","MSFT","GOOGL","AMZN"]
prices = {ticker: random.uniform(100, 500) for ticker in TICKERS}

async def send_stock_update(websocket):
    print("Client connected.")
    try:
        while True:
            ticker = random.choice(TICKERS)
            old_price = prices[ticker]
            new_price = round(old_price * random.uniform(0.98, 1.02), 2)
            prices[ticker] = new_price

            data = {
                "ticker": ticker,
                "price": new_price,
                "timestamp": datetime.now().isoformat()
            }

            await websocket.send(json.dumps(data))
            await asyncio.sleep(1)
    except Exception as e:
        print(f"Connection error: {e}")

async def main():
    async with serve(send_stock_update, "", 8001):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
