# James Gardner


import numpy
import cv2

img1 = cv2.imread("TestImages/SnowLeo2.jpg")
cv2.imshow("SnowLeo2.jpg" , img1)
cv2.waitKey(0)
blankImg = numpy.zeros((500, 500, 3), numpy.uint8)
cv2.imshow("SnowLeo2.jpg", blankImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
