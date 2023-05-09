import cv2

# 加载原始水印图像和提取出来的水印图像
img1 = cv2.imread('original_watermark.png')
img2 = cv2.imread('extracted_watermark.png')

# 计算MSE
# mse = ((img1 - img2) ** 2).mean()

# 计算PSNR
# psnr = cv2.PSNR(img1, img2)

# 计算SSIM
# ssim = cv2.SSIM(img1, img2, multichannel=True)

# 打印相似度指标
# print('MSE:', mse)
# print('PSNR:', psnr)
# print('SSIM:', ssim)


tmp = cv2.bitwise_and(img1, img2)
cv2.imshow('tmp', tmp)
cv2.waitKey(0)
cv2.destroyAllWindows()

