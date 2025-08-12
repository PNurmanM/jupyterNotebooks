from ultralytics import YOLO

import torch
import torchvision


print(torch.cuda.is_available())



#model = YOLO(f'oldbest.pt')

model = YOLO('yolov8m-seg .pt')

results = model.predict(0, show=True, device=0, conf=0.5)