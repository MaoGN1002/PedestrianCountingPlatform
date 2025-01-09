# def predict(visible_image_path, infrared_image_path):

#     return 111


import cv2  # 假设使用 OpenCV 进行图像处理
import numpy as np
import logging
from PIL import Image, ImageDraw, ImageFont
# 配置日志记录
logging.basicConfig(level=logging.DEBUG)

def predict(visible_image_path, infrared_image_path):
    image=Image.open(visible_image_path)
    # 在图像右上方写一个 "1"
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text = "1"
    text_size = draw.textsize(text, font=font)
    position = (image.width - text_size[0] - 10, 10)  # 右上角，距离边缘 10 像素
    draw.text(position, text, font=font, fill="red")
    
    # 保存处理后的图像
    processed_image_path = visible_image_path.replace(".jpg", "_processed.jpg")
    image.save(processed_image_path)
    return processed_image_path
