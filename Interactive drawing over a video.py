#Drawing on a video interactively
import cv2 as cv

#callback function to draw a rectangle
def draw_rectangle(event,x,y,flags,param):
    global pt1,pt2,topleft_clicked,botright_clicked
    if event == cv.EVENT_LBUTTONDOWN:

        #Reset the rectangle(check whether rectangle has already been drawn)
        if topleft_clicked == True and botright_clicked == True:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topleft_clicked = False
            botright_clicked = False

        #Rectangle hasn't been drawn
        if topleft_clicked == False:
            pt1 = (x,y)
            topleft_clicked = True

        elif botright_clicked == False:
            pt2 = (x,y)
            botright_clicked = True

#global variable
pt1 = (0,0) #top left of the rectangle
pt2 = (0,0) #bottom right of the rectangle
topleft_clicked = False
botright_clicked = False

#connect to callback
cap = cv.VideoCapture(0)
cv.namedWindow('Test')
cv.setMouseCallback('Test',draw_rectangle)

while True:
    ret,frame = cap.read()

    #drawing on the frame based off the global variable
    if topleft_clicked == True:
        cv.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)

    if topleft_clicked and botright_clicked:
        cv.rectangle(frame,pt1,pt2,(0,0,255),3)

    cv.imshow('frame',frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()