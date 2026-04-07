# Real-Time Object Detection Using OpenCV

## 1. Project Overview
This project is a beginner-friendly, real-time object detection system built using Python and OpenCV. It utilizes the lightweight but powerful **YOLOv8n** (You Only Look Once, Nano version) pre-trained model to detect and label common objects live through the laptop's built-in webcam.

**Why is object detection useful?**
Object detection allows computers to "see" and locate objects in an image or video stream. By drawing a bounding box around the object and identifying what it is, machinery and programs can interact automatically with physical things.

**Where can it be used in real life?**
- Self-driving cars (detecting pedestrians, traffic lights, and other vehicles).
- Security systems (identifying unauthorized individuals).
- Medical imaging (spotting anomalies in scans).

**Why is this a good student mini-project?**
It bridges theoretical computer vision concepts into a tangible, fast, and visual demonstration. The code is modular, well-commented, and easily executable without needing complex cloud services or heavy GPUs.

---

## 2. Project Features
- **Real-Time Webcam Detection:** Accesses the native laptop webcam instantly.
- **Multiple Object Detection:** Can find several objects in the same frame simultaneously.
- **Bounding Box Drawing:** Clean, colored rectangles drawn around detected objects.
- **Class Label Display:** Prints exactly what the object is (e.g., person, bottle, chair, laptop).
- **Confidence Score Display:** Shows how certain the model is about its prediction (e.g., 0.85 for 85%).
- **Dynamic FPS Counter:** Displays Frames Per Second continually in the corner.
- **On-Screen Object Count:** Dynamically updates the total number of items currently in the frame.
- **Easy Exit Key:** Smooth shutdown by pressing `q`.

---

## 3. Folder Structure
```text
object_detection_project/
│
├── main.py               # The main Python code connecting the webcam to the YOLO model
├── requirements.txt      # List of necessary libraries to run the project
├── README.md             # This documentation file
└── yolov8n.pt            # The neural network weights file (auto-downloaded on first run)
```

---

## 4. Setup and Installation Steps

> **Note:** The steps below are meant for a Windows PC. 

**Pre-requisites:** Install Python on your system.
1. Download Python from [python.org](https://www.python.org/downloads/).
2. Run the installer. **CRITICAL:** Check the box that says "Add Python to PATH" before clicking Install.

**Steps to Prepare the Project:**
1. Open up **Command Prompt** or **Terminal**.
2. Navigate to this project folder using the `cd` command. Example:
   ```bash
   cd "OneDrive\Documents\object detection"
   ```
3. Install the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

---

## 5. How to Run

1. Open your terminal in the project folder.
2. Run the application with the command:
   ```bash
   python main.py
   ```
3. **What happens next:**
   * A Python window will open.
   * Your webcam light will turn on.
   * A pop-up window named "Real-Time Object Detection" will appear.
   * Put an object (like your phone, a bottle, or yourself) in front of the camera, and it will draw a purple box over it with its name.
4. **To Quit:** Simply select the webcam window and press the lowercase `q` key on your keyboard.

---

## 6. Working Explanation
When you execute the program, the following sequence happens:
1. **Webcam Capture:** OpenCV connects to your camera (ID 0) and begins capturing raw video frames continuously.
2. **Model Processing:** Each frame is passed into the pre-trained `YOLOv8n` neural network. 
3. **Prediction:** The model analyzes the pixel data to predict coordinate boxes, a numeric Class ID (representing the object name), and a confidence probability.
4. **Drawing Output:** Using `cv2.rectangle` and `cv2.putText`, the program draws the bounding borders, labels, count, and FPS over the original frame.
5. **Real-time Loop:** The drawn image is shown instantly. This loop repeats roughly 15-30 times a second, giving the illusion of smooth video output.

---

## 7. Algorithm & Workflow

1. Start Program
2. Initialize OpenCV VideoCapture to access Webcam Source 0.
3. Load the pre-trained Ultralytics YOLOv8n Object Detection model.
4. **Loop Begins:** Capture a frame `img` from the webcam.
   - *Check Check:* If frame fails to load, `break` loop.
5. Provide `img` to the YOLO model to detect objects.
6. Retrieve a list of generic results (bounding boxes, class, confidence).
7. For each detected object:
   - Extract `(X1, Y1, X2, Y2)` coordinates.
   - Extract Class Name from the COCO dataset labels list.
   - Calculate precision probability (Confidence Score).
   - Draw Box and Label visually on `img`.
8. Calculate elapsed time for FPS.
9. Display FPS and Object Count on `img`.
10. Display `img` output window.
11. Check if the 'q' key is pressed. If yes, `break` loop.
12. **Loop Ends**
13. Stop webcam stream and securely close windows.

---

## 8. Input / Output

**Input:**
* A continuous live feed of RGB image matrices from the physical USB or Built-in Webcam.

**Output:**
* A real-time modified video stream window detailing:
  - Bounding Boxes mapped accurately over objects.
  - Text Labels citing Object Name and Model Confidence percentage.
  - A real-time diagnostic overlay (FPS and Total Items present).

---

## 9. Real-World Applications

* **Smart Surveillance:** Flagging when unauthorized vehicles or unrecognized persons enter restricted boundaries.
* **Retail Monitoring:** Automatically counting items on a shelf or monitoring queue lines at cash registers.
* **Smart Homes:** Triggering outdoor security lights specifically when a person walks near the door, not when a tree branch moves.
* **Assistive Technology:** Translating visual surrounds into audio queues to help visually impaired individuals navigate a room.
* **Traffic Systems:** Intelligent traffic lights that change dynamically by counting waiting cars versus relying purely on timed loops.

---

## 10. Limitations

* **Lighting Dependancy:** In low-light or backlit environments, edge detection fails, resulting in drastically lower accuracy.
* **Webcam Constraints:** Blurry or low-resolution webcams yield messy pixel data, confusing the AI.
* **Distance:** Very small or distant objects, as well as heavily occluded (hidden) items, might not be picked up by the lightweight `YOLOv8n`.
* **Hardware Overhead:** While lightweight, running computer vision on older CPU-only systems can cause high heat and lower framerates.

---

## 11. Future Enhancements

* **Custom Object Training:** Re-training the model weights to recognize entirely new objects specific to a domain (e.g., detecting defects in manufacturing items).
* **Face Detection Integration:** Expanding the base person detector into active facial recognition against a personnel database.
* **Automated Object Logging:** Logging the detection counts over time into an Excel sheet to create business metrics.
* **Security Alerts:** Connecting an SMTP service to auto-email a screenshot whenever a specific object (like an unattended bag) is seen.
* **Mobile Camera Support:** Tapping into phone sensors (via IP Webcam apps) to use this setup fully wirelessly.
