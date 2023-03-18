#!/bin/bash

echo "Apply database migrations"
alembic upgrade head

echo "Start server"
uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --reload
