from ast import Break
import cv2 as cv
from cv2 import waitKey

# Capturing Video
video = cv.VideoCapture("resources/tech.mp4")

# Running Indicators to show errors
if (video.isOpened()==False):
    print("There is error")


# Reading and playing our videos
while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        cv.imshow("Frame",frame)
        cv.waitKey(1)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

video.release()
cv.destroyAllWindows()
