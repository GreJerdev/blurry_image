from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
import api.services.image_service as image_service




class WordCloudService:
    

    def create_wordCloud(self, text):
        image_ser = image_service.ImageService()
        img = image_ser.genarate_image()
        img_mask = np.array(img)

        wc = WordCloud(stopwords=STOPWORDS,
        mask=img_mask,
        background_color="white",
        contour_color="white",
        contour_width=1
        ).generate(text)
        return wc.to_image()