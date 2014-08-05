# James Gardner

import cv2

img1 = cv2.imread("TestImages/SnowLeo1.jpg")
cv2.imshow("Leopard 1", img1)
img2 = cv2.imread("TestImages/SnowLeo2.jpg")
cv2.imshow("Leopard 2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
