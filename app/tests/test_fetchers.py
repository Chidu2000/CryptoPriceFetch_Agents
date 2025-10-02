from app.fetchers.fetch_prices import fetch_market_chart_hourly
from app.fetchers.fetch_news import fetch_and_store_feeds

def test_fetch_prices():
    df = fetch_market_chart_hourly("bitcoin", days=1)
    assert not df.empty
    assert "timestamp" in df.columns and "price" in df.columns

def test_fetch_news():
    fetch_and_store_feeds(limit=3)  # just check no exceptions
