# import necessary libraries
import cv2 as cv

# reading images 
img = cv.imread("resources/logo.png")

# resizing images
re_size = cv.resize(img, (500,500))

# converting images to gray scale
img_grey = cv.cvtColor(re_size, cv.COLOR_BGR2GRAY)

# showing images
cv.imshow("LOGO Window",img_grey)

# Lock Pop Window for time
cv.waitKey(0)
