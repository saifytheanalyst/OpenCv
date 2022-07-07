# import necessary libraries
import cv2 as cv
import numpy as np

# load image from resources
img = cv.imread("resources/saify.jpg")

# resizing image
img = cv.resize(img, (300,300))

# grey image
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# black and white image
thresh,black_white = cv.threshold(grey_img, 127, 255, cv.THRESH_BINARY)

# blurred image
blurr_img = cv.GaussianBlur(img,(23,7),0)

# Edge Detection
edge_img = cv.Canny(img, 23,23)

# thickness of lines
mat_kernal = np.ones((3,3), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernal), iterations=1)

# Make Thinner Lines
ero_img = cv.erode(dilated_img, mat_kernal, iterations=1)

# Crop Images
crop_img = img[0:300,70:300]

# load and display image
cv.imshow("Origional", img)
cv.imshow("Resized", img)
cv.imshow("Grey Image", grey_img)
cv.imshow("Black & White", black_white)
cv.imshow("Blurred Image", blurr_img)
cv.imshow("Edge Image", edge_img)
cv.imshow("Dilated Image", dilated_img)
cv.imshow("Erotated Image", ero_img)
cv.imshow("Cropped Image", crop_img)
cv.waitKey(0)
cv.destroyAllWindows()