import re
from flask import request
import os
import urllib.request
from api.services.check_image import ImageProcessing
from PIL import Image
  
# open method used to open different extension image file


from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import torch

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def check_image(name):

		# Model
	model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

	# Image
	im = 'https://ultralytics.com/images/zidane.jpg'
	im = Image.open(r"D:\\Projects\\python\\image_blurry\\code\\api\services\\luxemburg_passport.jpg") 

	
	# Inference
	results = model(im)
	res = results.pandas().xyxyn[0].to_json(orient = "records")
	results.show()
	print(res)
	return(res)
	if request.is_json == False:
		return {"error":"the request should be a json with file 'name' and 'image' as string base64"}
	
	image_name = request.json["name"]
	image = request.json["image"]

	ip = ImageProcessing(image_name,image)
	return {"status":"SUCCESS"}
    