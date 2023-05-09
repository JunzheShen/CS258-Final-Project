# Dirty Paper Precoding
import numpy as np
from skimage import data
import matplotlib.pyplot as plt
from PIL import Image
import cv2
def dirty_paper_code(y, T):
    return (y + T/2) % T - T/2

wm = cv2.imread("watermark2.png",cv2.IMREAD_GRAYSCALE)
# wm = wm.convert("L").resize((512,512))
im = cv2.imread("Lenna.png",cv2.IMREAD_GRAYSCALE)

T = 20

s = dirty_paper_code(wm-im, T)
im_wm = im + s
wm_ex = -dirty_paper_code(im_wm + np.random.rand(*im.shape), T)
fig, (ax_wm, ax_im, ax_im_wm, ax_wm_ex)=plt.subplots(nrows = 1,ncols = 4, figsize = [20,20])
ax_wm.imshow(wm, cmap = plt.cm.gray)
ax_wm.set_xlabel('wm')
ax_im.imshow(im, cmap = plt.cm.gray)
ax_im.set_xlabel('im')
ax_im_wm.imshow(im_wm, cmap = plt.cm.gray)
ax_im_wm.set_xlabel('im_wm')
ax_wm_ex.imshow(wm_ex, cmap = plt.cm.gray)
ax_wm_ex.set_xlabel('wm_ex')
with open('./output/with_noise_hiding.txt', 'w') as f:
    def to_str(line):
        line = [str(i) for i in line]
        return ' '.join(line) + '\n'
    f.writelines([to_str(line) for line in wm_ex])
plt.show()
# cv2.imshow('image', wm_ex)
# cv2.imwrite('./output/with_noise.png', 255*wm_ex)
# cv2.waitKey()
