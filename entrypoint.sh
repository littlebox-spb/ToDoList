#!/bin/bash
cd /opt/todolist || exit 1
python manage.py makemigrations
status=$?
if [[ $status != 0 ]]; then
python manage.py migrate
fi
exec "$@"
