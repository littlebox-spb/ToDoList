#!/bin/bash
python manage.py migrate --check # Проверка миграций
status=$? # Проверяем наличие новых миграций
if [[ $status != 0 ]]; then # Если есть новые миграции
  python manage.py makemigrations # Подготовка миграций
  python manage.py migrate # Выполнение миграций
fi # Завершаем условие
exec "$@" # Запуск основной команды
