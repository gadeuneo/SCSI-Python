#James Gardner

import cv2
import numpy

img1 = cv2.imread("TestImages/Puzzle1.jpg")
grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cannyImg = cv2.Canny(grayImg, 100, 200)
lines = cv2.HoughLinesP(cannyImg, 1, numpy.pi/180, 5, 20, 10)
for lineSet in lines:
    for line in lineSet:
        cv2.line(img1, (line[0], line[1]), (line[2], line[3]),
                 (255, 255, 0))
cv2.imshow("HoughLines", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
