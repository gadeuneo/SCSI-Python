#James Gardner

import cv2
import numpy

speed = 2

img = cv2.imread("TestImages/SnowLeo2.jpg")
cv2.imshow("Original", img)


#cv2.imshow("Original", img)

(rows, cols, depth) = img.shape

while (True):
    code = cv2.waitKey(0)
    char = chr(code & 0xFF)   
    
    if char == 'r':
        speed += 5
        rotMat = cv2.getRotationMatrix2D( (cols / 2, rows / 3), speed, 1)
        rotImg = cv2.warpAffine(img, rotMat, (cols,rows))
        cv2.imshow("Rotated", rotImg)
        cv2.waitKey(1)
    elif char == 'e':
        speed += 10
        rotMat = cv2.getRotationMatrix2D( (cols / 2, rows / 3), speed, 1)
        rotImg = cv2.warpAffine(img, rotMat, (cols,rows))
        cv2.imshow("Rotated", rotImg)
        cv2.waitKey(1)
    elif char == 't':
        speed += 2
        rotMat = cv2.getRotationMatrix2D( (cols / 2, rows / 3), speed, 1)
        rotImg = cv2.warpAffine(img, rotMat, (cols,rows))
        cv2.imshow("Rotated", rotImg)
        cv2.waitKey(1)
    elif char == 'w':
        speed += 50
        rotMat = cv2.getRotationMatrix2D( (cols / 2, rows / 3), speed, 1)
        rotImg = cv2.warpAffine(img, rotMat, (cols,rows))
        cv2.imshow("Rotated", rotImg)
        cv2.waitKey(1)
    elif char == 'q':
        break
cv2.destroyAllWindows()
