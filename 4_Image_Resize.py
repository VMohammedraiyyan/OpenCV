# Importing Library
import cv2

# To Read Image
cat = cv2.imread("C:/Users/ELCOT/Desktop/cat.jpg")

# To Print Shape
print(cat.shape)

# To Show the Image
cv2.imshow("Cat", cat)

# 1. To Resize the Image
catResize = cv2.resize(cat, (600,600))

catResizeA = cv2.resize(cat, (600,600), interpolation = cv2.INTER_AREA)

catResizeC = cv2.resize(cat, (600,600), interpolation = cv2.INTER_CUBIC)

# INTER_AREA is used for shrinking, whereas the INTER_CUBIC is used for zooming

# To Print Shape of the Resized Image
print(catResize.shape)

# To Show the Resized Image
cv2.imshow("Resized Cat", catResize)

cv2.imshow("Resized Image using INTER_AREA", catResizeA)

cv2.imshow("Resized Image using INTER_CUBIC", catResizeC)

# 2. To Crop Image
catCrop = cat[0:500, 200:800]

# To Show the Cropped Image
cv2.imshow("Cropped Cat", catCrop)

# To Delay
cv2.waitKey(0)