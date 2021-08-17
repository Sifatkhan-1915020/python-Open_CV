import cv2 as cv
import numpy as np

pic=cv.imread('back.jpg')

gray=cv.cvtColor(pic,cv.COLOR_BGR2GRAY)

cv.imshow('Picture',gray)

data_file=cv.CascadeClassifier('haar_face.xml')

face_det=data_file.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

print(f'total finding face is {len(face_det)}')
for(x,y,w,h) in face_det:
    cv.rectangle(pic,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
cv.imshow('Detect',pic)




cv.waitKey(0)