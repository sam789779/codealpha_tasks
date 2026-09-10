# Task 3 – Real-Time Object Detection and Tracking

## Description

This project performs real-time object detection and tracking using **YOLOv8**, **OpenCV**, and the **ByteTrack** tracking algorithm.

The program uses the computer's camera as the video source, detects objects in each frame, and tracks them in real time. The detected and tracked objects are displayed in a live window.

## Technologies Used

* Python
* OpenCV
* Ultralytics YOLOv8
* ByteTrack

## How It Works

1. Loads the YOLOv8 Nano model.
2. Opens the computer's camera using OpenCV.
3. Reads video frames continuously.
4. Detects and tracks objects using YOLOv8 and ByteTrack.
5. Displays the results with bounding boxes and tracking information.
6. Press **Q** to exit the program.

## Requirements

Install the required libraries:

```bash
pip install opencv-python ultralytics
```

The program uses the `yolov8n.pt` model.

## How to Run

Run the Python file:

```bash
python task3.py
```

Make sure your camera is available and working.

## Exit

Press **Q** while the detection window is active to stop the program.

## Author

Task 3 Submission
