# coingecko simple api

import requests
import pandas as pd
from app.db import Price, SessionLocal

def fetch_market_chart_hourly(symbol, days=1,vs_currency="usd"):
    """
    symbol_id: coin id on coingecko, e.g., 'bitcoin', 'ethereum'
    days: how many days of history
    returns pandas DataFrame with timestamp, price
    """
    coingecko_url = "https://api.coingecko.com/api/v3"
    
    url = f"{coingecko_url}/coins/{symbol}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}
    response = requests.get(url, params=params,timeout=30)
    response.raise_for_status()  # raise an exception if the request fails
    
    data = response.json()
    prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    prices["timestamp"] = pd.to_datetime(prices["timestamp"])
    return prices[["timestamp", "price"]]

def store_price_point(symbol, timestamp, price, volume=None):
    
    session = SessionLocal()
    p = Price(symbol=symbol, timestamp=timestamp, open=price, high=price, low=price, close=price, volume=volume or 0.0)
    session.add(p)
    session.commit()
    session.close()
    