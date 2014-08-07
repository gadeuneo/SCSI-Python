import cv2
import numpy as np

startPt = None
endPt = None

# mouse callback function
def drawBox(event,x,y,flags,param):
    global startPt
    global endPt

    if event == cv2.EVENT_LBUTTONDOWN:
        if startPt == None:
            startPt = (x, y)
        elif endPt == None:
            endPt = (x, y)
            cv2.rectangle(img, startPt, endPt, (255, 255, 0))
        else:
            print "both defined"

# Create a black image, a window and bind the function to window

cap = cv2.VideoCapture(0)
cv2.namedWindow('Video')
cv2.setMouseCallback('Video',drawBox)

while(1):
    r, img = cap.read()
    cv2.imshow('Video',img)
    if startPt != None and endPt != None:
        if startPt[1] < endPt[1]:
            roi = img[startPt[1]:endPt[1], startPt[0]:endPt[0]]
        else:
            roi = img[endPt[1]:startPt[1], endPt[0]:startPt[0]]
        cv2.imshow("Selected part", roi)
    
    x = cv2.waitKey(20) & 0xFF
    if x == 27:
        break
    elif x == ord(' '):
        startPt = None
        endPt = None
        cv2.closeWindow("Selected part")
    elif x == ord('s'):
        cv2.imwrite("saved.jpg", roi)
        startPt = None
        endPt = None
        cv2.closeWindow("Selected part")
        

        
        
cap.release()    
cv2.destroyAllWindows()
