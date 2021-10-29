import cv2
import numpy as np

cat = cv2.imread("C:\\Users\\ELCOT\\Desktop\cat.jpg")
cv2.imshow("Cat", cat)

# Joining Image Horizontally
catHor = np.hstack((cat, cat))
cv2.imshow("Horizontal Image", catHor)

# Joining Image Vertically
catVer = np.vstack((cat,cat))
cv2.imshow("Vertical Image", catVer)

cv2.waitKey(0)

# The Problem with this technique is that We can't join Two Different images. We can only join same Image.
