

import cv2


cap = cv2.VideoCapture(0)

frameNum = 0
filenameTemplate = "SavedImages/frame{:04d}.jpg"
key = ' '
while key != 'q':
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    fileName = filenameTemplate.format(frameNum)
    cv2.imwrite(fileName, frame)
    x = cv2.waitKey(30)
    key = chr(x & 0xFF)
    frameNum = frameNum + 1
    
cv2.destroyAllWindows()
