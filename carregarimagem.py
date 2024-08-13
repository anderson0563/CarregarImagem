import cv2
import numpy as np

# Read input image
img = cv2.imread('image.png')

# Mirror in x direction (flip horizontally)
imgX = np.flip(img, axis=1)
# imgX = imgX = img[:, ::-1, :]

# Mirror in y direction (flip vertically)
imgY = np.flip(img, axis=0)
# imgY = img[::-1, :, :]

# Mirror in both directions (flip horizontally and vertically)
imgXY = np.flip(img, axis=(0, 1))
# imgXY = img[::-1, ::-1, :]

# Outputs
cv2.imwrite('flipX.png', imgX)
cv2.imwrite('flipY.png', imgY)
cv2.imwrite('flipXY.png', imgXY)