import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")

video_path = 0  
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

print("Processing video stream... Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("End of video stream or failed to read frame.")
        break
    results = model.track(frame, persist=True, tracker="bytetrack.yaml")
    annotated_frame = results[0].plot()
    cv2.imshow("Real-Time Object Detection & Tracking", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows(
