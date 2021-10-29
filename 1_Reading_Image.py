# Importing Library
import cv2

'''
READING AN IMAGE:

* Syntax - cv2.imread(path, flag)

# path => where the image is located;
# flag =>
cv2.IMREAD_COLOR    # flag = 1 (for colored image)
cv2.IMREAD_GRAYSCALE  # flag = 0 (for gray image)
cv2.IMREAD_UNCHANGED
'''

# To Read Image
img = cv2.imread("C:/Users/ELCOT/Desktop\/cat.jpg")

'''
DISPLAYING AN IMAGE:

* Syntax - cv2.imshow(window_name, image)
'''

# To show the Image
cv2.imshow("Cat", img)
cv2.waitKey(0)