#!/bin/sh

[ -z "$PORT" ] && PORT=8000
[ -z "$WORKERS" ] && WORKERS=4
[ -z "$LOG_LEVEL" ] && LOG_LEVEL=info

APPLICATION_ASGI="config.asgi:fastapp"
APPLICATION_TIMEOUT=30

echo "🚀 Running FastAPI App..."
echo " • ASGI:      $APPLICATION_ASGI"
echo " • Timeout:   $APPLICATION_TIMEOUT"
echo " • Port:      $PORT"
echo " • Workers:   $WORKERS"
echo " • Log Level: $LOG_LEVEL"
echo "────────────────────────────────────────────"

uvicorn config.asgi:fastapp --host 0.0.0.0 --port ${PORT} --reload

#exec gunicorn "$APPLICATION_ASGI" \
#    --timeout "$APPLICATION_TIMEOUT" \
#    --graceful-timeout 30 \
#    --access-logfile - \
#    --error-logfile - \
#    --log-level "$LOG_LEVEL" \
#    --worker-class uvicorn.workers.UvicornWorker \
#    --workers "$WORKERS" \
#    --bind "0.0.0.0:$PORT"
