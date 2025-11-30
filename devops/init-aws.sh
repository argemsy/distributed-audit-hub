#!/bin/bash
set -e
set -x

MAX_RETRIES=30
DELAY=2
RETRIES=0

echo "Esperando LocalStack..."

until awslocal sqs list-queues >/dev/null 2>&1; do
  if [ "$RETRIES" -ge "$MAX_RETRIES" ]; then
    echo "❌ Timeout esperando LocalStack. Abortando."
    exit 1
  fi
  RETRIES=$((RETRIES+1))
  echo "   > reintentando ($RETRIES/$MAX_RETRIES)..."
  sleep $DELAY
done

echo "LocalStack disponible!"

### Create SQS queue if not exists
if ! awslocal sqs get-queue-url --queue-name audit-hub-events >/dev/null 2>&1; then
  awslocal sqs create-queue --queue-name audit-hub-events
  echo "🟢 Cola SQS creada: audit-hub-events"
else
  echo "🟡 Cola SQS ya existe, saltando..."
fi

### Create S3 Bucket if not exists
if ! awslocal s3 ls | grep -q audit-files; then
  awslocal s3 mb s3://audit-hub-files
  echo "🟢 Bucket S3 creado: audit-hub-files"
else
  echo "🟡 Bucket S3 ya existe, saltando..."
fi

echo "✨ Local AWS infra ready!"
