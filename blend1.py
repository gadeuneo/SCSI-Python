#James Gardner

import cv2
import numpy
image = cv2.imread("TestImages/shops.jpg")
(bc, gc, rc) = cv2.split(image)

cv2.imshow("Blue channel", bc)
cv2.imshow("Green channel", gc)
cv2.imshow("Red channel", rc)
cv2.waitKey(0)

zc = numpy.zeros( bc.shape, numpy.uint8 )
blueImg = cv2.merge((bc, zc, zc))
cv2.imshow("Blue channel", blueImg)
greenImg = cv2.merge((zc, gc, zc))
cv2.imshow("Green channel", greenImg)
redImg = cv2.merge((zc, zc, rc))
cv2.imshow("Red channel", redImg)
cv2.waitKey(0)

blend = cv2.addWeighted(greenImg, 0.5,
                blueImg, 0.5,
                0)
cv2.imshow("blend",blend)
cv2.waitKey(0)


cv2.destroyAllWindows()
