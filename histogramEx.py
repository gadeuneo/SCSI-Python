#James Gardner

import cv2
import numpy

cv2.calcHist(images,channels,mask,histSize,ranges)
cv2.calcBackProject(images,channels,hist,ranges,scale)
cv2.compareHist(hist1,hist1,method)
cv2.equalizeHist(image)
cv2.normalize(src,dst,alpha,beta,norm_type,dtype)
