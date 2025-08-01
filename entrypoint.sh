#!/bin/sh

sleep 3

python manage.py migrate

python -m gunicorn sharecode.asgi:application \
    --workers 1 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8001 \
    --timeout 60 &
python -m uvicorn sharecode.asgi:application --port=8002 &
python -m celery -A sharecode.celery:app worker --concurrency=1 --queues=high_priority,low_priority --loglevel=INFO &
wait