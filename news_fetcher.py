import requests
from database import SessionLocal, NewsArticle
from datetime import datetime

API_KEY = "ac459e3e4a26482d9fb6477cc40b75bc"
NEWS_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + API_KEY

def fetch_news():
    response = requests.get(NEWS_URL)
    data = response.json()
    
    if data.get("articles"):
        db = SessionLocal()
        for article in data["articles"][:5]:
            published_at = datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")

            existing_article = db.query(NewsArticle).filter(NewsArticle.url == article["url"]).first()

            if not existing_article:
            
                news_item = NewsArticle(
                    title=article["title"],
                    description=article.get("description"),
                    url=article.get("url"),
                    published_at=published_at 
                )
                db.add(news_item)
        db.commit()
        db.close()
