#Drawing over images using mouse(w/o draggin)
import cv2 as cv
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),100,(0,255,0),-1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)


cv.namedWindow(winname='Image')
cv.setMouseCallback('Image',draw_circle)

#Blank image
img = np.zeros((512,512,3),np.int8)

while True:
    cv.imshow('Image',img)
    key = cv.waitKey(1)
    if key == ord('q'):
        # Once you enter 'q' the window will be destroyed
        break

cv.destroyAllWindows()


