#!/bin/sh

[ -z "$PORT" ] && PORT=8000
[ -z "$WORKERS" ] && WORKERS=4

echo "🚀 Running FastAPI App..."
echo " • Port:    $PORT"
echo " • Workers: $WORKERS"
echo "──────────────────────────────"

exec gunicorn config.asgi:fastapp \
    --timeout 30 \
    --graceful-timeout 30 \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    --worker-class uvicorn.workers.UvicornWorker \
    --workers "$WORKERS" \
    --bind "0.0.0.0:$PORT"
