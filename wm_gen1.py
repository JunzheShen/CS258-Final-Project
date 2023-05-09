import numpy as np
import matplotlib.pyplot as plt
import cv2

# 生成高斯分布随机数
mean = 255 / 2
std = 255/2
size = (512, 512)
gaussian_array = np.random.normal(loc=mean, scale=std, size=size)
gaussian_array = np.uint8(gaussian_array)

# 将随机数可视化为图像
cv2.imwrite('watermark1.png', gaussian_array)


