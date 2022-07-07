# import necessary libraries
import cv2 as cv
import numpy as np

# capture camera
cap = cv.VideoCapture(0) #webcam no. 0

# indicators
if cap.isOpened() == False:
    print("There is an error")
    
# read webcam untill end
while cap.isOpened():
    ret, frame = cap.read()
    if ret==True:
        cv.imshow("Frame", frame)
        
        # Press q for exit
        if cv.waitKey(1) & 0xFF== ord('q'):
            break
    else:
       break
    

# Relsease or close windows easily
cap.release()
cv.destroyAllWindows()

