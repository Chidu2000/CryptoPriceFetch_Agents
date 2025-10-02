
from transformers import pipeline

_sentiment = pipeline('sentiment-analysis')

def analyze_sentiment(texts):
    response = _sentiment(texts)
    
    return [
        {"text":t,"label":r["label"],"score":r["score"]} for t,r in zip(texts,response)
    ]
    