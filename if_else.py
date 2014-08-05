# James Gardner

import cv2


img1 = cv2.imread("TestImages/SnowLeo1.jpg")
cv2.imshow("Pic 1", img1)
cv2.waitKey(0)

img2 = cv2.imread("TestImages/SnowLeo2.jpg")

cv2.imshow("Pic 1", img2)
cv2.waitKey(0)

img2 = cv2.imread("TestImages/Puzzle1.jpg")

cv2.imshow("Pic 1", img2)
cv2.waitKey(0)

img2 = cv2.imread("TestImages/Coins1.jpg")

cv2.imshow("Pic 1", img2)
cv2.waitKey(0)

cv2.destroyAllWindows()
