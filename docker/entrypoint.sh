#!/bin/bash
set -e

if [ "$1" = 'runserver' ]; then
    sleep 1
    alembic upgrade head
    exec flask run -h 0.0.0.0 -p 5050
else
    exec "$@"
fi
