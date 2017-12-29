#coding:utf8
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv2.imread('021.jpg',0)
imgf = np.fft.fft2(img) #二维离散傅立叶变换
imgfshift = np.fft.fftshift(imgf) #直流分量移到频谱中心
imgr = np.real(imgfshift)
imgi = np.imag(imgfshift)
img_rst = np.sqrt(imgr*imgr+imgi*imgi)#计算频谱幅值
print img_rst
#rst = (img_rst-min(min(img_rst)))/(max(max(img_rst))-min(min(img_rst)))*225#归一化
rst = np.log(np.abs(img_rst))
plt.imshow(rst,'gray')
plt.show()