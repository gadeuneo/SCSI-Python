#James Gardner

import cv2
import numpy


img = cv2.imread("TestImages/SnowLeo2.jpg")
cv2.imshow("Original", img)
(rows, cols, depth) = img.shape

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)

code = cv2.waitKey(0)
char = chr(code & 0xFF)

if char == 'a':
    transMatirx = numpy.float32([[1,0,30], [0,1,0]])
    transImag = cv2.warpAffine(img, transMatrix, (cols, rows))
    cv2.imshow("Translated", transImag)
elif char == 'w':
    transMatrix = numpy.float32([[1,0,0], [0,1,30]])
    transImag = cv2.warpAffine(img,transMatrix, (cols,rows))
    cv2.imshow("Translated", transImag)
elif char == 'd':
    transMatrix = numpy.float32([[1,0,-30], [0,1,0]])
    transImag = cv2.warpAffine(img, transMatrix, (cols,rows))
    cv2.imshow("Translated", transImag)
elif char == 's':
    transMatirx = numpy.float32([[1,0,0], [0,1,-30]])
    transImag = cv2.warpAffine(img,transMatrix, (cols,rows))
    cv2.imshow("Translated", transImag)



transMatrix = numpy.float32([[1, 0, 30], [0, 1, 50]])
transImag = cv2.warpAffine(img, transMatrix, (cols, rows))
cv2.imshow("Translated", transImag)
