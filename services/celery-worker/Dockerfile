FROM python:3.14.2-slim

WORKDIR /app

COPY ../../backend/pyproject.toml .
COPY ../../backend/poetry.lock .

# RUN pip install poetry && \
#     poetry config virtualenvs.create false && \
#     poetry install --no-dev

RUN poetry config virtualenvs.create false \
 && poetry lock --no-update \
 && poetry install --no-root --no-interaction --no-ansi

COPY ../../backend/app ./app

CMD ["celery", "-A", "app.tasks.tasks", "worker", "--loglevel=info"]