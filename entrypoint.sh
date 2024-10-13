#!/bin/bash

# Переход в нужную директорию
cd /opt/todolist || exit 1

# Проверка миграций
python manage.py migrate --check
status=$?

if [[ $status != 0 ]]; then
  # Выполнение миграций, если есть изменения
  python manage.py migrate
fi

# Запуск основной команды
exec "$@"
