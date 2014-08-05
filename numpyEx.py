#James Gardner

import cv2
import numpy
image = cv2.imread("TestImages/SnowLeo4.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", gray)
blackImg = numpy.zeros((150, 250), numpy.uint8)
cv2.imshow("Blank image", blackImg)
