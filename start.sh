#!/bin/bash
celery -A celery_worker worker --loglevel=info &
celery -A celery_worker beat --loglevel=info &
uvicorn main:app --reload
