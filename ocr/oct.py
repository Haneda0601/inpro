import os
from PIL import Image
import sys
import pyocr
import pyocr.builders
import cv2
import numpy as np

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]

# 画像設定
image = cv2.imread('./images/mojigazou_test2.png')

# 画像の黒い部分を強調する＆黒っぽくない部分を全て白に変更
black = [155, 155, 155]
white = [255, 255, 255]
image[np.where((image >= black).all(axis=2))] = white

# 黒っぽい部分を黒に強調する
blackflg = [169, 169, 169]
black = [0, 0, 0]
image[np.where((image <= blackflg).all(axis=2))] = black

# 画像の大きさを1.5倍に
img_org = cv2.resize(image , (int(image.shape[1]*1.5), int(image.shape[0]*1.5)))

# 一度画像を生成する
cv2.imwrite('./images/cv2_img.jpg', img_org)

img_rgb = Image.open("./images/cv2_img.jpg").convert("RGB")

text = tool.image_to_string(
    img_rgb,
    lang='jpn',
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
f = open('./images/test.txt', 'w')
f.write(text)
f.close()

os.remove('./images/cv2_img.jpg')
# print(text)
