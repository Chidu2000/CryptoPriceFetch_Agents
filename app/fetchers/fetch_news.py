
import feedparser
import datetime
from app.db import News, SessionLocal

COIN_FEEDS = {
    "bitcoin": [
        "https://news.google.com/rss/search?q=bitcoin",
        "https://cryptonews.com/rss/bitcoin-news"
    ],
    "ethereum": [
        "https://news.google.com/rss/search?q=ethereum",
        "https://cryptonews.com/rss/ethereum-news"
    ],
    # add more coins as needed
}

def fetch_and_store_feeds(coin: str, limit: int = 20):
    session = SessionLocal()
    feeds = COIN_FEEDS.get(coin.lower(), [])
    stored_feeds = []
    
    if not feeds:
        print(f"No feeds configured for {coin}")
        return

    for feed in feeds:
        parsed = feedparser.parse(feed)
        for entry in parsed.entries[:limit]:
            title = entry.title
            content = entry.get("summary") or entry.get("description") or "" 
            published = getattr(entry, "published_parsed", None)
            if published:
                published_at = datetime.datetime(*published[:6])
            else:
                published_at = datetime.now()

            n = News(
                title=title,
                source=feed,
                published_at=published_at,
                content=content,
            )
            session.add(n)
            stored_feeds.append(n.title)

    session.commit()
    session.close()
    return stored_feeds