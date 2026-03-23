from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = "postgresql://postgres:admin123@db:5432/ai_green_corridor"
    
    # RabbitMQ settings
    RABBITMQ_URL: str = "amqp://guest:guest@rabbitmq:5672/"
    
    # MinIO settings
    MINIO_URL: str = "http://minio:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    
    # Celery settings
    CELERY_BROKER_URL: str = RABBITMQ_URL
    CELERY_RESULT_BACKEND: str = RABBITMQ_URL

    class Config:
        env_file = ".env"

settings = Settings()