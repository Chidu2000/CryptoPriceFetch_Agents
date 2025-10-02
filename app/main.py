# app/main.py
from fastapi import FastAPI
from app.agent import run_pipeline

app = FastAPI(title="Crypto Market Intelligence Agent")

# --- Simple endpoint for analysis ---
@app.get("/analyze/{coin}")
def analyze_coin(coin: str):
    
    """
    Returns structured JSON:
    - signal
    - confidence
    - summary bullets
    - sentiment analysis
    """
    return run_pipeline(coin)

# --- Background daily task ---
@app.on_event("startup")
def start_scheduler():
    import threading, time

    def daily_task():
        from app.agent import run_pipeline
        coins = ["bitcoin", "ethereum", "solana"]
        while True:
            for coin in coins:
                result = run_pipeline(coin)
                print(f"Daily report for {coin}: {result['signal']} @ {result['latest_price']}")
            time.sleep(30)  # every 24h

    threading.Thread(target=daily_task, daemon=True).start()
