from celery import Celery

celery_app = Celery('tasks', broker='pyamqp://guest:guest@rabbitmq//')

@celery_app.task
def process_video(video_path):
    # Placeholder for video processing logic
    # This function would typically call the YOLO model to analyze the video
    print(f"Processing video: {video_path}")
    # Simulate detection result
    return {"status": "success", "message": "Video processed successfully."}

@celery_app.task
def send_notification(user_id, message):
    # Placeholder for sending notifications
    print(f"Sending notification to user {user_id}: {message}")
    return {"status": "success", "message": "Notification sent."}