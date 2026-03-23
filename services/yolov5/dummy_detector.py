def dummy_detection(video_path):
    # This function simulates the detection of an ambulance in a video.
    # In a real scenario, you would load a YOLO model and perform inference on the video frames.
    
    # For demonstration purposes, we will randomly decide if an ambulance is detected.
    import random
    import time

    time.sleep(2)  # Simulate processing time

    # Randomly return True or False to simulate detection
    detected = random.choice([True, False])
    return detected


if __name__ == "__main__":
    # Example usage
    video_path = "path/to/video.mp4"  # Replace with actual video path
    result = dummy_detection(video_path)
    if result:
        print("Ambulance detected! Sending green signal to traffic control.")
    else:
        print("No ambulance detected. No action taken.")