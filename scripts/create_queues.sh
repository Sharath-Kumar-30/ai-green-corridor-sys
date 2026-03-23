#!/bin/bash

# Create RabbitMQ queues for the AI Green Corridor System

# Define the queues
declare -a queues=("ambulance_requests" "traffic_notifications" "hospital_notifications" "video_analysis")

# Loop through the queues and create them
for queue in "${queues[@]}"; do
    echo "Creating queue: $queue"
    curl -u guest:guest -X PUT "http://localhost:15672/api/queues/%2F/$queue" -H "Content-Type: application/json" -d '{"durable":true}'
done

echo "All queues created successfully."