#Drawing over images with a mouse while dragging

import numpy as np
import cv2 as cv

# True while mouse button down, false while mouse button up
drawing = False
ix = -1
iy = -1

def draw_rectangle(event,x,y,flag,params):
    global ix,iy,drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

    

cv.namedWindow(winname='Image')
cv.setMouseCallback('Image',draw_rectangle)

#Creating blank image
img = np.zeros((512,512,3))

while True:
    cv.imshow('Image',img)
    key = cv.waitKey(1)
    if key == ord('q'):
        break

cv.destroyAllWindows()