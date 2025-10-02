# app/predictor.py
import pandas as pd
from app.nlp.sentiment import analyze_sentiment

def sma_signal(prices: pd.Series, window=14):
    sma = prices.rolling(window).mean()
    if prices.iloc[-1] > sma.iloc[-1]:
        return "up"
    elif prices.iloc[-1] < sma.iloc[-1]:
        return "down"
    else:
        return "neutral"

def hybrid_signal(prices: pd.Series, headlines: list[str]):
    # SMA part
    sma = sma_signal(prices)

    # Sentiment part
    sentiments = analyze_sentiment(headlines)
    avg_score = sum(s["score"] for s in sentiments) / len(sentiments) if sentiments else 0.0
    overall_sent = "positive" if avg_score > 0.6 else "negative"

    # Combine
    if sma == "up" and overall_sent == "positive":
        return "BUY"
    elif sma == "down" and overall_sent == "negative":
        return "SELL"
    else:
        return "HOLD"
