import cv2 as cv
from cv2 import imshow

cap = cv.VideoCapture("resources/tech.mp4")

frameNr = 0
while True:
    ret, frame = cap.read()
    if ret==True:
        cv.imwrite(f"resources/frames/frame_{frameNr}.jpg", frame)
    else:
        break
    frameNr += 2

cap.release()
