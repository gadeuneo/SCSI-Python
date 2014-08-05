#James Gardner

import cv2
import numpy
img = cv2.imread("TestImages/SnowLeo2.jpg")
cv2.imshow("Original", img)
(rows, cols, depth) = img.shape
origPts = numpy.float32([[40, 40], [160, 40], [40, 160]])
newPts = numpy.float32([[10, 80], [180, 5], [35, 193]])
mat = cv2.getAffineTransform(origPts, newPts)
warpImg = cv2.warpAffine(img, mat, (cols, rows))
cv2.imshow("Warped", warpImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
