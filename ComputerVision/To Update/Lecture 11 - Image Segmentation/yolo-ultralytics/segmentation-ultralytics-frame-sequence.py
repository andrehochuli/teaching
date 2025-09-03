from ultralytics import YOLO
import cv2
import random
import numpy as np

# Load the YOLO segmentation model
yolo_model = YOLO('yolov8m-seg.pt')  # YOLOv8 Medium Segmentation Model

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

    # Run segmentation on the resized frame
    results = yolo_model(frame_resized)

    # Create color assignments for each class
    for class_id, class_name in yolo_model.names.items():
        if class_name not in class_colors:
            class_colors[class_name] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw all segmentations in the frame
    combined_image = frame_resized.copy()
    for result in results:
        for mask, class_id in zip(result.masks.data, result.boxes.cls):
            label = yolo_model.names[int(class_id)]
            color = class_colors[label]

            # Resize mask to match the frame dimensions if necessary
            mask_np = mask.cpu().numpy()  # Convert to NumPy array
            mask_resized = cv2.resize(mask_np, (combined_image.shape[1], combined_image.shape[0]), interpolation=cv2.INTER_NEAREST)

            # Apply mask to combined image
            combined_image[mask_resized == 1] = color

    # Show the frame with segmentations
    cv2.imshow('YOLO Segmentation - Video/Camera', combined_image)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
