

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == True:
        r2, dispImg = cv2.threshold(frame, 100, 180, cv2.THRESH_TOZERO)
        dispImg = cv2.flip(dispImg, flipCode=1)
        cv2.imshow("Thresholded", dispImg)
        num = cv2.waitKey(5) & 0xFF
        key = chr(num)
        if key == 'q':
            break

cap.release()
cv2.destroyAllWindows()
