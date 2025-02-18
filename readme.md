# News Fetcher Project

Overview
The News Fetcher is a Python-based project that fetches the latest news articles using the News API, stores them in a MySQL database, and runs periodically every minute using Celery. The project also exposes a FastAPI interface to fetch stored news articles and manually trigger the fetching of new ones.

# Features

Fetch Latest News: Fetches the latest news articles from the News API.
Store in MySQL Database: Saves fetched news articles to a MySQL database.
Periodic Task: Uses Celery to automatically fetch news every minute.
API Endpoints:
GET /news: Fetches stored news articles.
POST /fetch-news: Manually triggers the fetching of new news articles.

# Project Structure

news-fetcher-project/
│── main.py             # The FastAPI application with endpoints.
│── celery_worker.py    # Celery configuration and task handling.
│── news_fetcher.py     # Logic for fetching news articles from the News API.
│── database.py         # Database connection and session handling with SQLAlchemy.
│── requirements.txt    # Lists the required dependencies to install


# Install Dependencies
pip install -r requirements.txt


# Running the Application

1. To start all the necessary services (Celery worker, Celery Beat, and FastAPI), you can use the provided shell script start_services.sh.
    chmod +x start.sh

2. Run the shell script:
    ./start.sh


