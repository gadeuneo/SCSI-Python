#James Gardner

import cv2
import numpy

img = cv2.imread("TestImages/SnowLeo2.jpg")
cv2.imshow("Original", img)
(rows, cols, depth) = img.shape
transMatrix = numpy.float32([[1, 0, 30], [0, 1, 50]])
transImag = cv2.warpAffine(img, transMatrix, (cols, rows))
cv2.imshow("Translated", transImag)

cv2.waitKey(0)
cv2.destroyAllWindows()
