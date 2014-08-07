#James Gardner

import cv2
import numpy

lines = cv2.HoughLinesP(image, rho, theta,
                        threshold, minLineLen, maxLineGap)
