import numpy as np
from PIL import Image
import cv2

watermark = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

# 转换为NumPy数组
watermark_array = np.array(watermark)

# 计算所有像素值的平方的平均值
average_power = np.mean(watermark_array.astype(np.float64) ** 2)

print('Average power:', average_power)
print(np.var(watermark_array))