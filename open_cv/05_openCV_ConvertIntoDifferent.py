# import necessary libraries
import cv2 as cv

# capture webcam
cap = cv.VideoCapture(0)

# run loop to load and show webcam
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.resize(frame, (400,300))
    frame1 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if ret==True:
        
        cv.imshow("grey", frame1)
        cv.imshow("origional", frame)
        # Press q for exit
        if cv.waitKey(1) & 0xFF== ord('q'):
            break
    else:
       break

cap.release()
cv.destroyAllWindows()
