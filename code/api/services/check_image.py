
from io import BytesIO
import matplotlib.pyplot as plt
import PIL.Image
import base64
import sys
from PIL import Image
from io import BytesIO
import torch


class ImageProcessing:



    def __init__(self, name,image_data):
        self.name = name 
        self.image_data = base64.b64decode(image_data)
        stream = BytesIO(self.image_data)
        image = Image.open(stream).convert("RGBA")
        stream.close()
        #image.show()
       
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True,force_reload=True)
        img =Image.open('luxemburg_passport.jpg')
        results = model(img)  # includes NMS
        print("===========================================")
        
        print(results.pandas().xyxyn[0])
        print("===========================================")
        results.show()
        #self.image = PIL.Image.Image()

        #self.image.frombytes( self.image_data)
        #plt.show( self.image)