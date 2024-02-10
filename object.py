import cv2
import numpy as np
import torch
from pathlib import Path

# Set the path to the yolov5 repository
yolov5_path = Path("yolov5")

# Load the YOLOv5 model
model = torch.hub.load(str(yolov5_path), 'custom', path='yolov5s.pt', source='local')








# Load YOLOv4-tiny model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # You can specify 'yolov5s' or other versions

# # Set the model to inference mode
# model.eval()

# Define class names (YOLOv5)
class_names = model.names

# Function to perform object detection and find the object in the middle
def detect_and_find_middle_object(frame):
    # Perform object detection with YOLO
    results = model(frame)

    # Get detection results
    pred = results.pred[0]

    if len(pred) > 0:
        # Find the object with the highest confidence score
        max_confidence_idx = np.argmax(pred[:, 4])
        middle_object = pred[max_confidence_idx]

        # Extract object information
        x_center, y_center, width, height, confidence, class_id = middle_object

        # Calculate object coordinates
        x1, y1, x2, y2 = int(x_center - width / 2), int(y_center - height / 2), int(x_center + width / 2), int(y_center + height / 2)

        # Draw a bounding box around the object
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Display the class name and confidence score
        label = f'{class_names[int(class_id)]}: {confidence:.2f}'
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame,label

# Inside the video capture loop




# # Open a video capture
# cap = cv2.VideoCapture(0)  # Replace with 0 for camera or your video file

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Perform object detection on the frame
#     frame_with_middle_object = detect_and_find_middle_object(frame)

#     cv2.imshow('Object Detection', frame_with_middle_object)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
