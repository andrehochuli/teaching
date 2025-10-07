import cv2
import os
import random


# Open video file or camera
video_source = 0  # Set to 0 for webcam or replace with the path to a video file
cap = cv2.VideoCapture(video_source)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# Loop through each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    # Resize the frame for consistency
    frame_resized = cv2.resize(frame, (1024, 768))

     # Show the frame with detections
    cv2.imshow('YOLO Detection - Video/Camera', frame_resized)

    # Press 'q' to quit
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
