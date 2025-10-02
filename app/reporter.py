# app/reporter.py
import matplotlib.pyplot as plt
import matplotlib
import os
os.makedirs("reports", exist_ok=True)
matplotlib.use('Agg')

def plot_signals(prices, signals):
    """Plot price with BUY/SELL/HOLD markers."""
    plt.figure(figsize=(12,6))
    plt.plot(prices['timestamp'], prices['price'], label="Price")

    buy = [i for i,s in enumerate(signals) if s=="BUY"]
    sell = [i for i,s in enumerate(signals) if s=="SELL"]

    plt.scatter(prices['timestamp'].iloc[buy], prices['price'].iloc[buy],
                color='green', marker='^', label='BUY')
    plt.scatter(prices['timestamp'].iloc[sell], prices['price'].iloc[sell],
                color='red', marker='v', label='SELL')

    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.title("Price and Signals")
    plt.legend()
    plt.tight_layout()
    plt.savefig("reports/signals_plot.png")
    plt.close()
