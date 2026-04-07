import cv2
import math
import time
from ultralytics import YOLO
import cvzone
import numpy as np

# 1. INITIALIZE WEBCAM
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

# 2. LOAD PRE-TRAINED DETECTION MODEL (UPGRADED TO YOLOv8s)
# We upgraded to YOLOv8s.pt (Small instead of Nano). 
# It provides much higher accuracy with fewer false positives, 
# while still running very smoothly on a standard laptop.
model = YOLO("yolov8s.pt")

classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
    "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
    "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
    "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
    "teddy bear", "hair drier", "toothbrush"
]

prev_time = 0

print("Starting Professional Object Detection HUD... Press 'q' to exit.")

while True:
    success, img = cap.read()
    if not success:
        break

    # 3. RUN MODEL WITH A HIGHER CONFIDENCE THRESHOLD
    results = model(img, stream=True, verbose=False)
    
    object_count = 0

    # 4. DRAW SLEEK BOUNDING BOXES 
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Calculate confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            
            # FILTRATION: Only show highly confident objects (reduces jitter/noise)
            if confidence > 0.45:
                # Get Box Dimensions
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1
                
                # Get Class ID
                cls = int(box.cls[0])
                current_class = classNames[cls]

                # Draw Professional Corner Rectangles instead of basic boxes
                cvzone.cornerRect(img, (x1, y1, w, h), 
                                  l=30, t=5, rt=1, 
                                  colorR=(255, 0, 255), colorC=(0, 200, 0))
                
                # Draw sleek shaded background text using cvzone
                cvzone.putTextRect(img, f'{current_class} {confidence*100:.0f}%', 
                                   (max(0, x1), max(35, y1)), 
                                   scale=1.2, thickness=2, 
                                   colorT=(255, 255, 255), colorR=(255, 0, 255),
                                   font=cv2.FONT_HERSHEY_PLAIN, offset=6)
                
                object_count += 1

    # 5. RENDER PROFESSIONAL ON-SCREEN HUD (Heads-Up Display)
    new_time = time.time()
    fps = 1 / (new_time - prev_time) if (new_time - prev_time) > 0 else 0
    prev_time = new_time

    # Create a semi-transparent dark background for the metrics at the top right
    overlay = img.copy()
    cv2.rectangle(overlay, (img.shape[1] - 300, 20), (img.shape[1] - 20, 120), (0, 0, 0), cv2.FILLED)
    # Apply alpha blending
    img = cv2.addWeighted(overlay, 0.4, img, 0.6, 0)
    
    # Draw professional text over the semi-transparent box
    cv2.putText(img, f"Live FPS: {int(fps)}", (img.shape[1] - 280, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(img, f"Detections: {object_count}", (img.shape[1] - 280, 100), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Add Project Title watermark bottom left
    cv2.putText(img, "Project: Real-Time Object Detection", (20, img.shape[0] - 20), 
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

    # 6. DISPLAY OUTPUT
    cv2.imshow("Professional Object Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
