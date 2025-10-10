from ultralytics import YOLO
import cv2
import os
import random

# Load the model
# yolo_model = YOLO('yolov8n.pt')  # YOLOv8 Nano
# yolo_model = YOLO('yolov8s.pt')  # YOLOv8 Small
# yolo_model = YOLO('yolov8m.pt')  # YOLOv8 Medium
# yolo_model = YOLO('yolov8l.pt')  # YOLOv8 Large
# yolo_model = YOLO('yolov8x.pt')  # YOLOv8 Extra Large
yolo_model = YOLO('yolov8x.pt')  # Currently using YOLOv8 Medium

# Folder containing images
image_folder = 'data'

# Assign random colors to each class
class_colors = {}

# Loop through all images in the folder
for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, "office.jpg")
    if not os.path.isfile(image_path):
        continue

    # Read and resize the image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (640, 480))

    # Run prediction on the resized image
    results = yolo_model(image)

    # Draw all detections in one image
    combined_image = image.copy()
    for result in results:
        for box in result.boxes:
            label = yolo_model.names[int(box.cls)]  # Get the class label
            confidence = float(box.conf)  # Get the confidence score
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates

            # Assign a color to the class if not already assigned
            if label not in class_colors:
                class_colors[label] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            color = class_colors[label]

            # Draw rectangle on combined image
            cv2.rectangle(combined_image, (x1, y1), (x2, y2), color, 2)  # Draw the bounding box with the class-specific color and thickness 2

            # Create label text
            label_text = f'{label} {confidence:.2f}'

            # Put label text on combined image
            cv2.putText(combined_image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_PLAIN, 2.0, color, 2)  # Draw label text above the bounding box

    # Show the combined image with all detections
    cv2.imshow('YOLO Prediction - All Classes Combined', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Draw detections, class by class
    for result in results:
        for box in result.boxes:
            label = yolo_model.names[int(box.cls)]  # Get the class label
            confidence = float(box.conf)  # Get the confidence score
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates

            # Assign a color to the class if not already assigned
            if label not in class_colors:
                class_colors[label] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            color = class_colors[label]

            # Create a copy of the original image for each class
            class_image = image.copy()

            # Draw rectangle on class image
            cv2.rectangle(class_image, (x1, y1), (x2, y2), color, 2)  # Draw the bounding box with the class-specific color and thickness 2

            # Create label text
            label_text = f'{label} {confidence:.2f}'

            # Put label text on class image
            cv2.putText(class_image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_PLAIN, 2.0, color, 2)  # Draw label text above the bounding box

            # Show the frame for the current class
            cv2.imshow(f'YOLO Prediction - Class: {label}', class_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
