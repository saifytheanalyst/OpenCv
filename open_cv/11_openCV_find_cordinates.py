# step 1 import librareis
import cv2 as cv
import numpy as np

# step 2 Define function for finding co_ordinates
def find_cord(event, x,y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        # left mouse click
        print(x,'',y)
        # how to define and print on the same image
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x)+','+str(y), (x,y), font, 1, (149,158,0), thickness=2)
        # show the text on image and image itself
        cv.imshow("image", img)
    if event == cv.EVENT_RBUTTONDOWN:
        print(x,'',y)
        font = cv.FONT_HERSHEY_COMPLEX
        b = img[x,y,0]
        g = img[x,y,1]
        r = img[x,y,2]
        cv.putText(img, str(b)+','+str(g)+','+str(r), (x,y), font, 1, (255,0,0), thickness=2)
        cv.imshow("image", img)

# step 3 function to read and to display
if __name__ =='__main__':
    # read an image
    img = cv.imread("resources/logo.png")
    # show image
    cv.imshow("image",img)
    # setting call back function
    cv.setMouseCallback("image", find_cord)
    cv.waitKey(0)
    cv.destroyAllWindows()