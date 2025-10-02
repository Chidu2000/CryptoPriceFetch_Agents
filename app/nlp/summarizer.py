
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_API_KEY")
)

def summarize_news(news_items: list[str]) -> str:
    """Summarize list of headlines into 3 bullet points."""
    headlines = "\n".join([f"- {h}" for h in news_items])
    prompt = f"Summarize these crypto headlines into 3 concise insights:\n{headlines}"
    
    response = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages = [{"role":"user", "content":prompt}]
    )
    
    return response.choices[0].message.content.strip()
