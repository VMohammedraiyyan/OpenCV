# Importing Library
import cv2

vid = cv2.VideoCapture("C:/Users/ELCOT/Desktop/OpenCV/Resources/Video.mp4")

while True:
    isTrue, img = vid.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(20) & 0xFF==ord("s"):
        break

vid.release()
cv2.destroyAllWindows()