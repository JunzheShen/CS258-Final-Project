from skimage import io
from skimage.filters import rank
from skimage.measure import shannon_entropy

# 读取水印图像
wm = io.imread('watermark1.png', as_gray=True)

# 计算水印图像的熵值
wm_entropy = shannon_entropy(wm)
print(wm_entropy)