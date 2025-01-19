FROM python:3.12-slim

WORKDIR /opt/todolist

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHONPATH=/opt/todolist

RUN pip install "poetry==1.6.1"
RUN groupadd --system service && useradd --system -g service api

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-ansi --no-root

COPY src/todolist/ ./
COPY entrypoint.sh ./entrypoint.sh

RUN chmod +x entrypoint.sh  # Обеспечьте права на выполнение скрипта

USER api
ENTRYPOINT ["bash", "entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
