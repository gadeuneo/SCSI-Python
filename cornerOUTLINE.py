#James Gardner

import cv2
import numpy

img1 = cv2.imread("TestImages/Puzzle1.jpg")
grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
goodFeats = cv2.goodFeaturesToTrack(grayImg, 100, 0.1, 5)
