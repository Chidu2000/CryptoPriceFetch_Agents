import pandas as pd
from app.predictor import sma_signal, hybrid_signal

prices = pd.Series([1,2,3,4,5,6,7,8,9,10])

def test_sma_signal():
    result = sma_signal(prices)
    assert result in ["up", "down", "neutral"]

def test_hybrid_signal():
    headlines = ["Bitcoin surges", "Ethereum dips"]
    result = hybrid_signal(prices, headlines)
    assert result in ["BUY", "SELL", "HOLD"]
