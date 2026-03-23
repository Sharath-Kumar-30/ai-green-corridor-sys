FROM python:3.14.2-slim

# Set the working directory
WORKDIR /app

# Copy the poetry files
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN pip install poetry==1.8.0

RUN poetry config virtualenvs.create false \
 && poetry lock --no-update \
 && poetry install --no-root --no-interaction --no-ansi

# Copy the application code
COPY ./app ./app

# Copy the database initialization script
COPY ./db/init_db.sql ./db/init_db.sql

# Expose the FastAPI port
EXPOSE 8000

# Command to run the FastAPI application
ENTRYPOINT ["/start.sh"]
COPY start.sh /start.sh
RUN chmod +x /start.sh