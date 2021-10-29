import cv2
import numpy as np

# To Read Image
cat = cv2.imread("C:/Users/ELCOT/Desktop/cat.jpg")

# Gray-Scale Image
catGray = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)

# Blur Image
gaussianBlur = cv2.GaussianBlur(catGray, (11,11), 0)

# Median Blur
medianblur = cv2.medianBlur(cat, 5)

# Bilateral Filter
bilateral = cv2.bilateralFilter(cat, 9, 75, 75)

# Canny Image
catCanny = cv2.Canny(cat, 100, 100)

# Dilated Image
catDilate = cv2.dilate(catCanny, kernel=np.ones((5,5),np.uint8), iterations=1)

# Eroded Image
catErode = cv2.erode(catDilate, kernel=np.ones((6,6),np.uint8), iterations=1)

# To Show Normal Image
cv2.imshow("Cat", cat)

# To Show Gray-scale Image
cv2.imshow("Gray Image", catGray)

# To Show Blur-image
cv2.imshow("Blur Image", gaussianBlur)

cv2.imshow("Median Blur", cat)

cv2.imshow("Bilateral Filter", cat)

# To Show Canny Image
cv2.imshow("Canny Image", catCanny)

# To Show Dilated Image
cv2.imshow("Dilated Image", catDilate)

# To Show Eroded Image
cv2.imshow("Eroded Image", catErode)
cv2.waitKey(0)