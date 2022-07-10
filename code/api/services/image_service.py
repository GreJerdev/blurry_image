from PIL import Image,ImageDraw,ImageFont
import math
from PIL import Image, ImageDraw,ImageFont


class ImageService:

    def genarate_image(self,  width = 1600, height = 1200):
        img = Image.new("RGB", (width , height),color='white')
        # create ellipse image
        img1 = ImageDraw.Draw(img)  
        shape = [(int(width*.05),int(height*0.4)), (int(height*.4),int(height*0.8))]
        img1.ellipse(shape, fill ="black", outline ="black")
        shape =  [(int(width*.2),int(height*0.2)), (int(width*.8),int(height*0.6))]
        img1.ellipse(shape, fill ="black", outline ="black")
        shape =  [(int(width*.6),int(height*0.4)), (int(width*.95),int(height*0.8))]
        img1.ellipse(shape, fill ="black", outline ="black")
        shape =  [(int(width*.2),int(height*0.5)), (int(width*.8),int(height*0.95))]
        img1.ellipse(shape, fill ="black", outline ="black")
        return img