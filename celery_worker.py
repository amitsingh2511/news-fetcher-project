from celery import Celery
from news_fetcher import fetch_news
from celery.schedules import crontab

celery = Celery(
    "tasks",
    broker="sqla+sqlite:///celerydb.sqlite", 
    backend="db+sqlite:///celery_results.sqlite"
)

@celery.task(name="fetch_news_task")
def fetch_news_task():
    fetch_news()

celery.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "fetch_news_task",
        "schedule": crontab(minute="*"),
    }
}

celery.conf.timezone = "UTC"
