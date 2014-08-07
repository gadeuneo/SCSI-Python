#James Gardner

import cv2
import numpy


img = cv2.imread("TestImages/SnowLeo2.jpg")
cv2.imshow("Original", img)
(rows, cols, depth) = img.shape


while (True):

    code = cv2.waitKey(0)
    char = chr(code & 0xFF)
    
    if char == 'a':
        transMatrix = numpy.float32([[1,0,-10], [0,1,0]])
        transImag = cv2.warpAffine(img, transMatrix, (cols, rows))
        cv2.imshow("Translated", transImag)
    elif char == 'w':
        transMatrix = numpy.float32([[1,0,0], [0,1,-10]])
        transImag = cv2.warpAffine(img,transMatrix, (cols,rows))
        cv2.imshow("Translated", transImag)
    elif char == 'd':
        transMatrix = numpy.float32([[1,0,10], [0,1,0]])
        transImag = cv2.warpAffine(img, transMatrix, (cols,rows))
        cv2.imshow("Translated", transImag)
    elif char == 's':
        transMatrix = numpy.float32([[1,0,0], [0,1,10]])
        transImag = cv2.warpAffine(img,transMatrix, (cols,rows))
        cv2.imshow("Translated", transImag)
    elif char == 'q':
        break
    img = transImag
cv2.destroyAllWindows()
