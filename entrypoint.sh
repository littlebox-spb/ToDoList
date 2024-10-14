#!/bin/bash
set -e
cd /opt/todolist || exit 1
python manage.py migrate
status=$?
if [[ $status != 0 ]]; then
  python manage.py migrate
fi
exec "$@"
