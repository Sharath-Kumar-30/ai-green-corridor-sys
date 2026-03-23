from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@postgres:5432/greencorridor")
    
    # RabbitMQ settings
    RABBITMQ_URL: str = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672//")
    
    # Redis settings
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379/0")
    
    # MinIO settings
    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", "minio:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_SECRET_KEY", "minioadmin123")
    MINIO_BUCKET: str = os.getenv("MINIO_BUCKET", "uploads")

    class Config:
        env_file = ".env"

settings = Settings()