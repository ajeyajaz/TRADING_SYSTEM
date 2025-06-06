import asyncio
import websockets
import json
from collections import deque
from datetime import datetime, timedelta

price_history = {}

async def process_messages():
    url = "ws://localhost:8001"
    async with websockets.connect(url) as websocket:
        while True:
            async for message in websocket:
                data = json.loads(message)
                ticker = data["ticker"]
                price = data["price"]
                timestamp = datetime.fromisoformat(data["timestamp"])

                if ticker not in price_history:
                    price_history[ticker] = deque([(timestamp, price)])
                else:
                    price_history[ticker].append((timestamp, price))

                cutoff = timestamp - timedelta(minutes=2)

                # remove outdated entry
                while price_history[ticker] and price_history[ticker][0][0] < cutoff:
                    price_history[ticker].popleft()

                
                # check price rannge
                if len(price_history[ticker]) > 1:
                    old_price = price_history[ticker][0][1]
                    if old_price > 0:
                        percent_change = ((price - old_price) / old_price) * 100
                        if percent_change >= 2:
                            print(f"[ALERT] {ticker} price increased by {percent_change:.2f}% within 2 minutes!")

asyncio.run(process_messages())
