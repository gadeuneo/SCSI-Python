#James Gardner

import cv2
import numpy
img = cv2.imread("TestImages/SnowLeo2.jpg")
cv2.imshow("Original", img)
(rows, cols, depth) = img.shape
rotMat = cv2.getRotationMatrix2D( (cols / 2, rows / 2), 45, 1)
rotImg = cv2.warpAffine(img, rotMat, (cols, rows))
cv2.imshow("Rotated", rotImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
