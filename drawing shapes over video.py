#Drawing a rectangle/shape over a video
import cv2 as cv

cap = cv.VideoCapture(0)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#Top left corner
x = width // 2
y = height // 2

#width and height of rectangle
w = width // 4
h = height // 4

#Bottom right corner x+w, y+h

while True:
    ret,frame = cap.read()
    cv.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=4)
    cv.imshow('frame',frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()