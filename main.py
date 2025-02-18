from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, NewsArticle
from celery_worker import fetch_news_task

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/news")
def get_news(db: Session = Depends(get_db)):
    return db.query(NewsArticle).all()


@app.post("/fetch-news")
def trigger_fetch():
    fetch_news_task.delay()
    return {"message": "Fetching news in the background"}