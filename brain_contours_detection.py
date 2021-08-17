import cv2 as cv
import numpy as np

Brain=cv.imread('brain.jpg')
cv.imshow('Brain Real Footage',Brain)

blank=np.zeros(Brain.shape,dtype='uint8')

Grey =cv.cvtColor(Brain,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Brain Photo',Grey)

canny=cv.Canny(Brain,125,175)
cv.imshow('Canny Pic of Brain',canny)


ret,thres=cv.threshold(Brain,145,145,cv.BORDER_DEFAULT)
cv.imshow('Thresold brain Picture',thres)

contour,hieraraches=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contour)} contours find here!!')

cv.drawContours(Brain,contour,-1,(0,0,255),1)
cv.imshow('Contour',Brain)

cv.drawContours(blank,contour,-1,(0,0,255),1)
cv.imshow('Outline Contour',blank)
cv.waitKey(0)