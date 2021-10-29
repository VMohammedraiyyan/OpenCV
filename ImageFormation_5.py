# Importing Library
import cv2
import numpy as np


# For Black Image
img = np.zeros((512,512))
print(img.shape)

cv2.imshow("Black Image",img)    # To Show Black Image


# For Blue Image
imgB = np.zeros((512,512,3), np.uint8)
imgB[:] = 255,0,0

cv2.imshow("Blue Image", imgB)    # To Show Blue Image

# For Green Image
imgG = np.zeros((512,512,3),np.uint8)
imgG[:] = 0,255,0

cv2.imshow("Green Image", imgG)   # To Show Green Image

# For Red Color
imgR = np.zeros((512,512,3),np.uint8)
imgR[:] = 0,0,255

cv2.imshow("Red Image", imgR)   # To Show Red Image

cv2.waitKey(0)