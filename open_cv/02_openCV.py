

import cv2 as cv

# read image
img = cv.imread("resources/saify.jpg")

# resiing images
img = cv.resize(img,(1000,1000))

# convert into Gray
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# convert image into Black and White
thresh,binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)


# show Image
cv.imshow("origional", img)
cv.imshow("Grey", img_gray)
cv.imshow("Black & White", binary)

cv.waitKey(0)
# cv.destroyAllWindows()

# save Image
cv.imwrite("resources/origional.jpg", img)
cv.imwrite("resouces/Grey.jpg", img_gray)
cv.imwrite("resources/Black&White.jpg", binary)

cv.imwrite("saify_gray.jpg", img_gray)