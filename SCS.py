# Dirty Paper Precoding
import numpy as np
import cv2
# from skimage import data
import matplotlib.pyplot as plt
from PIL import Image

def quantization(img, step):
    return step * np.floor(img / step + 1 / 2)

def embed(host, wm, key, quan_step, alpha):
    a = quan_step * (wm / 2 + key)
    tmp = alpha * (quantization(host - a, quan_step) + a - host)
    return host + tmp

def decode(received, key, quan_step):
    return quantization(received - quan_step * key, quan_step) + key * quan_step - received

wm = cv2.imread("testwm.png",cv2.IMREAD_GRAYSCALE)
im = cv2.imread("Lenna.png",cv2.IMREAD_GRAYSCALE)
shape = im.shape
quan_step = 50
alpha = 1.0
key = np.random.rand(*shape)


im_wm = embed(im, wm, key, quan_step, alpha)
mean = 5
std_dev = 5
distorted_im = im_wm + np.random.normal(mean, std_dev, size=shape)
wm_ex = decode(distorted_im, key, quan_step)

# cv2.imwrite('original_watermark.png', wm)
# cv2.imwrite('extracted_watermark.png', wm_ex)

fig, (ax_wm, ax_im, ax_im_wm, ax_wm_ex)=plt.subplots(nrows = 1,ncols = 4, figsize = [20,20])
ax_wm.imshow(wm, cmap = plt.cm.gray)
ax_wm.set_xlabel('watermark')
ax_im.imshow(im, cmap = plt.cm.gray)
ax_im.set_xlabel('host image')
ax_im_wm.imshow(im_wm, cmap = plt.cm.gray)
ax_im_wm.set_xlabel('watermarked image')
ax_wm_ex.imshow(wm_ex, cmap = plt.cm.gray)
ax_wm_ex.set_xlabel('extracted watermark')
# plt.imshow(s)
# print(np.max(wm))
# cv2.imshow('extracted_watermark.png', wm_ex)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
with open('./output/SCS.txt', 'w') as f:
    def to_str(line):
        line = [str(i) for i in line]
        return ' '.join(line) + '\n'
    f.writelines([to_str(line) for line in wm_ex])
# plt.savefig('./output/scs_4.png')
# plt.show()
cv2.imshow('image', wm_ex)
cv2.imwrite('./output/scs_testwm.png', 255*wm_ex)
cv2.waitKey()
