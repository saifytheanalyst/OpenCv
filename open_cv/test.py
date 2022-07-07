import cv2 as cv
import numpy as np
img1 = cv.imread("resources/logo.png")
img2 = cv.imread("resources/saify.jpg")

def ver_stack(foreground_image, background_image):

    foreground = cv.resize(foreground_image, (400,400))
    background = cv.resize(background_image, (400,400))
    ver_stack = np.vstack((foreground,background))
    cv.imshow('composited image',ver_stack )
    cv.waitKey(0)

ver_stack(img1,img2)