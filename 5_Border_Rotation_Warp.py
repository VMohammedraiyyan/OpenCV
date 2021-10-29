import cv2

path = "C:/Users/ELCOT/Desktop/cat.jpg"
window_name = "Original"
window_name1 = "Border"

# Read Image
cat = cv2.imread(path)

# Bordered Image
cat = cv2.copyMakeBorder(cat, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=1)


(rows, cols) = cat.shape[:2]
# Rotated Image
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)

# Warp Affine
res = cv2.warpAffine(cat, M, (cols, rows))

# Show image
cv2.imshow(window_name, cat)
cv2.imshow(window_name1, cat)

#cv2.imshow("Rotated Image", cat)

# Delay
cv2.waitKey(0)