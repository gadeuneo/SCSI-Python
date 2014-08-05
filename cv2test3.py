# James Gardner

import cv2

lst1 = ["SnowLeo1.jpg", "SnowLeo2.jpg", "Puzzle1.jpg", "Coins1.jpg", "Coins2.jpg", "DollarCoin.jpg", "frankenstein.jpg", "gorge.jpg", "ghostrider.jpg", "Puzzle2.jpg"]

for var in lst1:
    x = cv2.imread("TestImages/"+var)
    cv2.imshow("img", x)
    cv2.waitKey(0)
cv2.destroyAllWindows()
