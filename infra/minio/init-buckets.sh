#!/bin/sh

# Create MinIO buckets for the project
mc alias set myminio http://minio:9000 admin admin123

# Create buckets
mc mb myminio/ambulance-requests
mc mb myminio/traffic-videos
mc mb myminio/hospital-data

# Set bucket policies (optional)
mc policy set public myminio/ambulance-requests
mc policy set public myminio/traffic-videos
mc policy set public myminio/hospital-data

echo "MinIO buckets initialized."