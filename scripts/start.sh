#! /usr/bin/env sh

exec gunicorn --workers 4 --threads 4 -b $HOST:$PORT $APP_MODULE
