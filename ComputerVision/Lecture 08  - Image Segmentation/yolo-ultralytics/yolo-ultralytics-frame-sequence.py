from ultralytics import YOLO
import cv2
import random
import numpy as np

# Load the YOLO detection model
yolo_model = YOLO('yolov8m.pt')  # YOLOv8 Medium Detection Model

# Assign random colors to each class
class_colors = {}

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

    # Run detection on the resized frame
    results = yolo_model(frame_resized)

    # Create color assignments for each class
    for class_id, class_name in yolo_model.names.items():
        if class_name not in class_colors:
            class_colors[class_name] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw all detections in the frame
    for result in results:
        for box in result.boxes:
            label = yolo_model.names[int(box.cls)]  # Get the class label
            confidence = float(box.conf)  # Get the confidence score
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates

            # Assign color for the current class
            color = class_colors[label]

            # Draw rectangle and label on the frame
            cv2.rectangle(frame_resized, (x1, y1), (x2, y2), color, 2)
            label_text = f'{label} {confidence:.2f}'
            cv2.putText(frame_resized, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_PLAIN, 2.0, color, 2)

    # Show the frame with detections
    cv2.imshow('YOLO Detection - Video/Camera', frame_resized)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
