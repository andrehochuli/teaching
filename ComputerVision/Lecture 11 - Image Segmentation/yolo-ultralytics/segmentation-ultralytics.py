from ultralytics import YOLO
import cv2
import os
import random
import numpy as np

# Load the segmentation model
# yolo_model = YOLO('yolov8n-seg.pt')  # YOLOv8 Nano
# yolo_model = YOLO('yolov8s-seg.pt')  # YOLOv8 Small
# yolo_model = YOLO('yolov8m-seg.pt')  # YOLOv8 Medium
# yolo_model = YOLO('yolov8l-seg.pt')  # YOLOv8 Large
# yolo_model = YOLO('yolov8x-seg.pt')  # YOLOv8 Extra Large
yolo_model = YOLO('yolov8x-seg.pt')  # YOLOv8 Medium Segmentation

# Folder containing images
image_folder = 'data'

# Assign random colors to each class
class_colors = {}

# Loop through all images in the folder
for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    if not os.path.isfile(image_path):
        continue

    # Read and resize the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (1024, 768))

    # Run segmentation on the resized image
    results = yolo_model(image)

    # Create color assignments for each class
    for class_id, class_name in yolo_model.names.items():
        if class_name not in class_colors:
            class_colors[class_name] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw all segmentations in one image
    combined_image = image.copy()
    for result in results:
        for mask, class_id in zip(result.masks.data, result.boxes.cls):
            label = yolo_model.names[int(class_id)]
            color = class_colors[label]

            # Resize mask to match the image dimensions if necessary
            mask_np = mask.cpu().numpy()  # Convert to NumPy array
            mask_resized = cv2.resize(mask_np, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)

            # Apply mask to combined image
            combined_image[mask_resized == 1] = color

    # Show the combined image
    cv2.imshow('YOLO Segmentation - All Classes Combined', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
