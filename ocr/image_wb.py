import cv2
import numpy as np

image = cv2.imread('./images/card.jpg')
# 画像の黒い部分を白に置き換える
black = [155, 155, 155]
white = [255, 255, 255]
image[np.where((image >= black).all(axis=2))] = white

blackflg = [169, 169, 169]
black = [0, 0, 0]
image[np.where((image <= blackflg).all(axis=2))] = black

img_org = cv2.resize(image , (int(image.shape[1]*1.5), int(image.shape[0]*1.5)))

# 画像の表示
cv2.imshow("Image", image)

# キー入力待ち(ここで画像が表示される)
cv2.waitKey()