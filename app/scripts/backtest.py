# scripts/backtest.py
import pandas as pd
from app.predictor import hybrid_signal

def run_backtest(prices: pd.Series, news: list[str]):
    balance, position = 1000, 0
    actions = []

    for i in range(20, len(prices)):
        action = hybrid_signal(prices[:i], news)
        if action == "BUY" and balance > 0:
            position = balance / prices.iloc[i]
            balance = 0
        elif action == "SELL" and position > 0:
            balance = position * prices.iloc[i]
            position = 0
        actions.append(action)

    final_value = balance + position * prices.iloc[-1]
    return final_value, actions
