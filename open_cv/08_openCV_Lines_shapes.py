# import necessary libriaries
import cv2 as cv
from cv2 import rectangle
import numpy as np

# draw a canvas
img = np.zeros((600,600))

# Size of canvas
print(f"size of canvas is {img.shape}")

# Adding colors in canvas
color_img = np.zeros((600,600,3))
color_img[50:120] = 255,170,0

# Adding line
cv.line(color_img,(0,0),(300,300), (255,0,0),3)

# adding rectangle
cv.rectangle(color_img, (50,100),(300,300),(255,170,255),3) # draw rectange
cv.rectangle(color_img, (50,100),(300,300),(255,170,255),cv.FILLED) #fille rectange

# Adding circle
cv.circle(color_img,(400,300), 50, (255,170,155), 20) # draw circle
cv.circle(color_img,(400,300), 50, (255,170,155), cv.FILLED) # fill cirlce

# Adding texts
cv.putText(color_img, "Saify the analyst",(50,500), cv.FONT_HERSHEY_DUPLEX,2, (255,0,125))

# load and show image
cv.imshow("Canvas Black", img)
cv.imshow("Colored canvas", color_img)
cv.waitKey(0)
cv.destroyAllWindows()