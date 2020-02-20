# /home/aiyunji/cxj/json/mask_png/24w-1双顶径_json_label.png

import matplotlib.pyplot as plt
import cv2
#文件地址
imageAddress=""
img=cv2.imread("/home/aiyunji/Desktop/testdata/mask/1.png")
print(img.shape)

plt.imshow(img)
plt.show()
