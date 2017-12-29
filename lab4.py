#coding:utf8
import matplotlib.pyplot as plt
import numpy as np
import cv2

# 原图
img = cv2.imread('021.jpg',0)
plt.imshow(img,cmap='gray')
plt.show()
# 原直方图
plt.hist(img.ravel(),256,[0,256])
plt.show()

# 直方图均衡化
img_eq = cv2.equalizeHist(img)
plt.imshow(img_eq,cmap='gray')
plt.show()
# 均衡后的直方图
plt.hist(img_eq.ravel(),256,[0,256])
plt.show()
