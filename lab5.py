#coding:utf8
import matplotlib.pyplot as plt
import cv2

#加入高斯或Salt&Pepper噪声的图像
#img = cv2.imread('021_gauss.bmp')
img = cv2.imread('021_sp.bmp')
plt.imshow(img)
plt.show()

#3x3均值滤波
blurred = cv2.blur(img,(3,3))
plt.imshow(blurred)
plt.show()

#5x5均值滤波
blurred5 = cv2.blur(img,(5,5))
plt.imshow(blurred5)
plt.show()

#3x3中值滤波
med_blurred = cv2.medianBlur(img,3)
plt.imshow(med_blurred)
plt.show()

#4x4中值滤波
med_blurred4 = cv2.medianBlur(img,5)
plt.imshow(med_blurred4)
plt.show()