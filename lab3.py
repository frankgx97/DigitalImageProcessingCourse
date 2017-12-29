#coding:utf8
import numpy as np
from matplotlib import pyplot as plt
import cv2
import bisect

def imadjust(src, tol=1, vin=[0,255], vout=(0,255)):
    # src : input one-layer image (numpy array)
    # tol : tolerance, from 0 to 100.
    # vin  : src image bounds
    # vout : dst image bounds
    # return : output img

    dst = src.copy()
    tol = max(0, min(100, tol))

    if tol > 0:
        # Compute in and out limits
        # Histogram
        hist = np.zeros(256, dtype=np.int)
        for r in range(src.shape[0]):
            for c in range(src.shape[1]):
                hist[src[r,c]] += 1
        # Cumulative histogram
        cum = hist.copy()
        for i in range(1, len(hist)):
            cum[i] = cum[i - 1] + hist[i]

        # Compute bounds
        total = src.shape[0] * src.shape[1]
        low_bound = total * tol / 100
        upp_bound = total * (100 - tol) / 100
        vin[0] = bisect.bisect_left(cum, low_bound)
        vin[1] = bisect.bisect_left(cum, upp_bound)

    # Stretching
    scale = (vout[1] - vout[0]) / (vin[1] - vin[0])
    for r in range(dst.shape[0]):
        for c in range(dst.shape[1]):
            vs = max(src[r,c] - vin[0], 0)
            vd = min(int(vs * scale + 0.5) + vout[0], vout[1])
            dst[r,c] = vd
    return dst

img = cv2.imread('021.jpg',0)
# 显示直方图
plt.hist(img.ravel(),256,[0,256])
plt.show()

# 灰度变换（负片）
img_reverse = img
img_reverse = abs(255 - img_reverse)
plt.imshow(img_reverse,cmap='gray')
plt.show()
# 显示直方图
plt.hist(img_reverse.ravel(),256,[0,256])
plt.show()

# 灰度变换
img_adj = imadjust(img, 1, [128,191],(0,255))
plt.imshow(img_adj,cmap='gray')
plt.show()

#转换为8位图
img_8bit = img_adj.convert('L') #convert可选参数为 ：1，L，P，RGB，RGBA，CMYK，YCbCr，I，F
plt.imshow(img_8bit,cmap = "gray")
plt.show()