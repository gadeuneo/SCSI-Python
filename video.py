#James Gardner

import cv2
vidCap = cv2.VideoCapture(0)
if vidCap.isOpened():
    ret, img = vidCap.read()
    cv2.imshow("Webcam", img)
    cv2.waitKey(0)
else:
    print "No camera connected"
cv2.destroyAllWindows()
vidCap.release()
