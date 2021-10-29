import cv2

img = cv2.imread("C:/Users/ELCOT/Downloads/kids.jpeg")
B, G, R = cv2.split(img)

cv2.imshow("Original",img)
cv2.waitKey(0)

cv2.imshow("BLUE", B)
cv2.waitKey(0)

cv2.imshow("GREEN", G)
cv2.waitKey(0)

cv2.imshow("RED", R)
cv2.waitKey(0)

cv2.destroyAllWindows()