import cv2
import numpy as np

# Creating a Black Image
img = np.zeros((640, 480))
cv2.imshow("Image", img)

# To Print Shape
print(img.shape)

# To Draw a Line in the Image
imgL = cv2.line(img, (20,30), (200,300), (25,255,255), 6)
#Syntax: cv2.line(img,(starting_pt),(Ending_pt),(Color),Thickness)
cv2.imshow("Lined Image", imgL)

# To Draw a Diagonal Line in the Image
imgD = cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (255,255,255), 5)
cv2.imshow("Diagonal Line", imgD)

# To Draw a Rectangle in the Image
imgR = cv2.rectangle(img, (0,0), (200,300), (255,255,255))
#Syntax: cv2.rectangle(img, (starting_pt), (Ending_pt), (Color), Thickness)
cv2.imshow("Rectangle Image", imgR)

# To Draw a Filled Rectangle
imgFR = cv2.rectangle(img, (60,70), (500,350), (255,255,255), cv2.FILLED)
#Syntax: cv2.rectangle(img, (starting_pt), (Ending_pt), (Color), cv2.FILLED)
cv2.imshow("Filled Rectangle", imgFR)

# To Draw a Circle
imgC = cv2.circle(img, (400,50), 30, (255,255,255), 2)
#Syntax: cv2.circle(img, (circle_pt), radius, (color), thickness)
cv2.imshow("Circle Image", imgC)

# To Text in an Image
imgT = cv2.putText(img, "OPENCV", (100,20), cv2.FONT_ITALIC, 1, (255,255,255), 2)
#Syntax: cv2.putText(img, , cv2.FONT, Font_scale, Color, Thickness)
cv2.imshow("Text Image", imgT)

cv2.waitKey(0)