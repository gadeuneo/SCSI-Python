#James Gardner

import cv2
import numpy

img = cv2.imread("TestImages/shops.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
cv2.imshow("img",img)
