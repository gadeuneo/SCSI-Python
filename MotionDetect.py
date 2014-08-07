

import cv2

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
if ret == True:
    while True:
        ret, frame2 = cap.read()
        if ret == True:
            img3 = cv2.absdiff(frame1, frame2)
            img3 = cv2.flip(img3, flipCode = 1)
            cv2.imshow("Difference", img3)
            frame1 = frame2
        num = cv2.waitKey(5) & 0xFF
        key = chr(num)
        if key == 'q':
            break

cap.release()
cv2.destroyAllWindows()
