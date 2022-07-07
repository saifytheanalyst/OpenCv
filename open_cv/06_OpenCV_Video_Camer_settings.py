# import libraries
import cv2 as cv

# capture camera
cap = cv.VideoCapture(0)

# setting the camera
cap.set(10,100) # 10 is the keys to set brightness
cap.set(3,1920) # widhth
cap.set(4,1080) # Height

while(True):
    ret, frame = cap.read()
    if ret==True:
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break 
    else:
        break

cap.release()
cv.destroyAllWindows()