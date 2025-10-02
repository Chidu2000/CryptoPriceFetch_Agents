# app/agent.py
from app.fetchers.fetch_prices import fetch_market_chart_hourly
from app.fetchers.fetch_news import fetch_and_store_feeds
from app.nlp.summarizer import summarize_news
from app.nlp.sentiment import analyze_sentiment
from app.predictor import hybrid_signal
from app.db import log_prediction, SessionLocal
from app.reporter import plot_signals
from datetime import datetime

def run_pipeline(coin: str, log=True):
    """
    Full agent pipeline:
    1. Fetch prices & news
    2. Summarize news with LLM
    3. Analyze sentiment
    4. Run hybrid SMA+sentiment predictor
    5. Log metrics
    6. Generate plots
    """

    # --- Fetch Data ---
    prices_df = fetch_market_chart_hourly(coin, days=5)
    news_items = fetch_and_store_feeds(coin, limit=10)  # list of dicts with 'title'

    # --- NLP Processing ---
    headlines = [str(n.title) for n in news_items ] if news_items else []
    if headlines:
        summary = summarize_news(headlines)
        sentiments = analyze_sentiment(headlines)
        confidence = max(s['score'] for s in sentiments)
    else:
        summary = ""
        sentiments = []
        confidence = 0.0

    # --- Prediction ---
    signal = hybrid_signal(prices_df['price'], headlines)

    # --- Log Metrics ---
    if log:
        db = SessionLocal()
        log_prediction(
            db=db,
            symbol=coin,
            timestamp=datetime.now(),
            pred_label=signal,
            probability=confidence,
            ground_truth=None,  # fill later if backtesting
            correct=None
        )
        db.close()
    # --- Generate Plots ---
    plot_signals(prices_df, [signal]*len(prices_df))  # placeholder

    # --- Output structured JSON ---
    return {
        "coin": coin,
        "signal": signal,
        "confidence": confidence,
        "summary": summary,
        "sentiments": sentiments,
        "latest_price": prices_df['price'].iloc[-1]
    }
