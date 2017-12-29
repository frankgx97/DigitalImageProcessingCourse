#coding:utf8
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

img = cv2.imread('021.jpg')
img_bg = cv2.imread('bg.jpg')

#加
img_dst = cv2.add(img, img_bg)
cv2.imshow('img_dst',img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#减
img_dst = cv2.subtract(img, img_bg)
cv2.imshow('img_dst',img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('021.jpg',0)

# 加
img_bright = cv2.add(img,50)
cv2.imshow('img_bright',img_bright)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 减
img_dark = cv2.subtract(img,50)
cv2.imshow('img_dark',img_dark)
cv2.waitKey(0)
cv2.destroyAllWindows()
#乘
img_mul = cv2.multiply(img, 1.5)
cv2.imshow('img_mul',img_mul)
cv2.waitKey(0)
cv2.destroyAllWindows()
#除
img_div = cv2.divide(img, 2)
cv2.imshow('img_div',img_div)
cv2.waitKey(0)
cv2.destroyAllWindows()
#四则运算
img = cv2.imread('021.jpg')
img_rst = img*1.1 + img_bg/3 -50
cv2.imshow('img_rst',img_rst)
cv2.waitKey(0)
cv2.destroyAllWindows()