#!/bin/bash -e

cd /app
gunicorn "app:app" \
    --bind "0.0.0.0:${PORT:-5000}" \
    --log-level INFO \
    --worker-class gevent \
    --worker-connections 768
