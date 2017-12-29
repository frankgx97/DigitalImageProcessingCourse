#coding:utf8
import numpy as np
import cv2

#打开图像
img = cv2.imread('021.jpg')

# 图像尺寸
print img.shape
# 图像大小
print img.size
# 图像类型
print img.dtype

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_matrix = np.array(img)

# 拆分为rgb
img_r = img_matrix[:, :, 0]
img_g = img_matrix[:, :, 1]
img_b = img_matrix[:, :, 2]

img_rgb = cv2.merge((img_b,img_g,img_r))
cv2.imshow('img_rgb', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

#另存为bmp
cv2.imwrite("021_bmp.bmp",img)

# 转为灰度图像
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('img_gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 转为二值图像
img_bin = cv2.threshold( img_gray, 100,255,cv2.THRESH_BINARY )[1]
cv2.imshow('img_bin', img_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()