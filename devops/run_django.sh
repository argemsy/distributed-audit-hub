#!/bin/sh

# Set defaults
[ -z "$PORT" ] && PORT=8000
[ -z "$WORKERS" ] && WORKERS=4

echo "🚀 Running Django ASGI App..."
echo "◽ Port: $PORT"
echo "◽ Workers: $WORKERS"

exec gunicorn config.asgi:application \
    --worker-class=uvicorn.workers.UvicornWorker \
    --workers="$WORKERS" \
    --bind="0.0.0.0:$PORT"
