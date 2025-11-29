#!/bin/sh

FAILURE_FILE=".failure"

echo "Junit Path: $JUNIT_PATH"
echo "Coverage Path: $COVERAGE_PATH"

poetry install --with dev --no-root;

echo "Running tests"
pytest --cov --junitxml="$JUNIT_PATH" || echo "There are failures in the tests" >> "$FAILURE_FILE"

echo "Running coverage"
coverage xml -o "$COVERAGE_PATH" || echo "There are failures in the tests" >> "$FAILURE_FILE"

if [ -f "$FAILURE_FILE" ]; then
    exit 1
fi
