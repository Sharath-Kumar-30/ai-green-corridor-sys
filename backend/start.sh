#!/usr/bin/env bash
set -e

echo "Waiting for Postgres..."
until pg_isready -h "${POSTGRES_HOST:-postgres}" -p 5432 -U "${POSTGRES_USER:-postgres}"; do
  sleep 1
done

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
#!/usr/bin/env bash
set -e

echo "Waiting for Postgres..."
until pg_isready -h "${POSTGRES_HOST:-postgres}" -p 5432 -U "${POSTGRES_USER:-postgres}"; do
  sleep 1
done

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
