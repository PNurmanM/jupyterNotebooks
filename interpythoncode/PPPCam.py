import cv2
import os
import supervision as sv
from ultralytics import YOLO
import numpy as np

model = YOLO(f'best.pt')
#model = YOLO(f'yolov9e-seg.pt')

cap = cv2.VideoCapture(0)

bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

if not cap.isOpened():
    print("No Cam")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, conf=0.25)[0]
    cv2.imshow('Webcam', results.plot())

    #detections = sv.Detections.from_ultralytics(results)

    #annotated_image = bounding_box_annotator.annotate(scene=frame, detections=detections)
    #annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    #cv2.imshow('Webcam', annotated_image)

    k = cv2.waitKey(1)

    if k == 27:
        print("Esc hit exiting...")
        break
    elif k == ord('s'):
        print("Ligma")

cap.release()
cv2.destroyAllWindows()