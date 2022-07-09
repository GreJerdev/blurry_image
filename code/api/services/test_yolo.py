import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True,force_reload=True)

# Images
imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

# Inference
results = model(imgs)

# Results
results.print()
results.show()  # or .show(), .save()

results.xyxy[0]  # img1 predictions (tensor)
results.pandas().xyxy[0]