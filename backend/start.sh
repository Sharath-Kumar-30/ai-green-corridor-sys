#!/usr/bin/env bash
set -e

echo "Waiting for Postgres..."
python - <<PY
import psycopg2
import os
import time
db_host = os.environ.get("POSTGRES_HOST", "postgres")
db_port = int(os.environ.get("POSTGRES_PORT", 5432))
db_user = os.environ.get("POSTGRES_USER", "postgres")
db_password = os.environ.get("POSTGRES_PASSWORD", "postgres")
db_name = os.environ.get("POSTGRES_DB", "greencorridor")
max_retries = 30
for i in range(max_retries):
    try:
        conn = psycopg2.connect(host=db_host, port=db_port, user=db_user, password=db_password, database=db_name)
        conn.close()
        print("PostgreSQL is ready!")
        break
    except psycopg2.OperationalError:
        if i < max_retries - 1:
            print(f"Postgres not ready, retrying... ({i+1}/{max_retries})")
            time.sleep(1)
        else:
            raise
PY

echo "Running alembic migrations..."
alembic upgrade head

echo "Ensuring MinIO bucket exists..."
python - <<PY
from minio import Minio
import os
c = Minio(os.environ.get("MINIO_ENDPOINT","minio:9000"), access_key=os.environ.get("MINIO_ACCESS_KEY","minioadmin"), secret_key=os.environ.get("MINIO_SECRET_KEY","minioadmin123"), secure=False)
bucket = os.environ.get("MINIO_BUCKET","uploads")
if not c.bucket_exists(bucket):
    c.make_bucket(bucket)
print("MinIO bucket ready:", bucket)
PY

echo "Running DB seed (if available)..."
python - <<PY
try:
    from app import seed
    seed.run()
except Exception as e:
    print('Seeding skipped or failed:', e)
PY

echo "Starting Uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

