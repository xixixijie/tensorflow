#查看mask

import matplotlib.pyplot as plt
import cv2
#文件地址
imageAddress="/home/aiyunji/Desktop/testdata/mask/1.png"
img=cv2.imread(imageAddress)
print(img.shape)

plt.imshow(img)
plt.show()
