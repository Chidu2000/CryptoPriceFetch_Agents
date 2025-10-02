# Crypto Market Intelligence Agent

A fully automated crypto market research agent that leverages real-time price data, news headlines, LLM summarization, sentiment analysis, and hybrid SMA-based predictions to provide actionable trading insights. Built for research, demo, and portfolio showcase, with metrics tracking and visual reports.

## Features
- Hybrid Predictor: Combines SMA (Simple Moving Average) price trends with NLP-based sentiment analysis for BUY / SELL / HOLD signals.
- LLM News Summarization: Uses OpenAI GPT OSS to summarize top crypto headlines into concise, actionable insights.
- Sentiment Analysis: Leverages Hugging Face transformers to evaluate positive/negative trends in news headlines.
- Real-time Data Fetching: Fetches market prices via CoinGecko and news via RSS feeds.
- Metrics Logging: Tracks predicted vs actual trends in a local DB for trend accuracy analysis.
- Visual Reports: Generates price + SMA + signals plots for easy interpretation.
- Automation & Scheduling: Runs daily tasks via FastAPI background threads; can be integrated with Cron or Airflow.
- Slack / Email Alerts (Optional): Push daily reports to a Slack channel or email.
- Backtesting: Historical backtesting to evaluate strategy performance and cumulative returns.

## Project Structure
crypto-agent/
├─ app/
│  ├─ main.py              # FastAPI app
│  ├─ agent.py             # Agent orchestration
│  ├─ fetchers/
│  │  ├─ fetch_prices.py
│  │  └─ fetch_news.py
│  ├─ predictor.py
│  ├─ reporter.py
│  ├─ db.py
│  └─ nlp/
│     ├─ summarizer.py
│     └─ sentiment.py
├─ scripts/
│  └─ backtest.py
├─ tests/
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
└─ README.md

## Setup & Installation
1. Clone the repository:
git clone https://github.com/Chidu2000/crypto-agent.git
cd crypto-agent

2. Install dependencies:
pip install -r requirements.txt

3. Run the FastAPI app:
uvicorn app.main:app --reload

4. Access the endpoint:
http://127.0.0.1:8000/analyze/bitcoin

5. Run backtesting script:
python scripts/backtest.py

## Docker Deployment
1. Build Docker image:
docker-compose build

2. Run container:
docker-compose up

The FastAPI app will be available at:
http://localhost:8000/analyze/bitcoin

## Example Output
{
  "coin": "bitcoin",
  "signal": "BUY",
  "confidence": 0.82,
  "summary": "- Bitcoin rallies past $60K\n- Ethereum dips amid regulatory concerns\n- Altcoins mixed performance",
  "sentiments": [
    {"text": "Bitcoin rallies past $60K", "label": "POSITIVE", "score": 0.95},
    {"text": "Ethereum dips amid regulatory concerns", "label": "NEGATIVE", "score": 0.88}
  ],
  "latest_price": 60250.5
}
