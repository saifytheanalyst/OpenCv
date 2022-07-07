import cv2 as cv
from cv2 import COLOR_BGR2GRAY
import numpy as np

face_cascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")


img = cv.imread("resources/faces.jpg")
img =cv.resize(img, (500,500))
img_grey = cv.cvtColor(img , COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_grey, 1.1, 4)

# draw a rectange
for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)



cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()