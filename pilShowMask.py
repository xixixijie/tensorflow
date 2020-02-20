# /home/aiyunji/cxj/json/mask_png/24w-1双顶径_json_label.png

import matplotlib.pyplot as plt
import cv2

img=cv2.imread("/home/aiyunji/Desktop/testdata/mask/10-02-08-刘巧珍_videoImg_17.png")
print(img.shape)

plt.imshow(img)
plt.show()