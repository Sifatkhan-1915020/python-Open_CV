import numpy as np
import cv2 as cv

cap=cv.VideoCapture(0)

ret,frame1=cap.read()
ret,frame2=cap.read()



while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),0)
    _,thresh=cv.threshold(blur,20,255,cv.THRESH_BINARY)
    dilate=cv.dilate(thresh,None,iterations=3)
    cntr,_=cv.findContours(dilate,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for i in cntr:
        (x, y, z, w)=cv.boundingRect(i)

        if cv.contourArea(i)<200 :
            continue

        cv.rectangle(frame1,(x,y),(x+z,y+w),(0,255,0),2)
        cv.putText(frame1,"status: {}".format('Movement'),(10,20),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)



    #cv.drawContours(frame1,cntr,-1,(255,0,0),2)

    cv.imshow("match",frame1)
    frame1=frame2
    ret,frame2=cap.read()

   


    if cv.waitKey(40) == 27 :
        break

cv.destroyAllWindows()
cap.release()
