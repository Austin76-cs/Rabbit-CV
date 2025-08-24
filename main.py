import cv2
from ultralytics import YOLO
import torch


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")
if device == 'cuda':
    print(f"Device name: {torch.cuda.get_device_name(0)}")
    
model = YOLO("best.pt")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    success, frame = cap.read()
    if success:
        results = model(frame, conf=0.35, device=device)

        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 Rabbit Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Exiting...")
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()