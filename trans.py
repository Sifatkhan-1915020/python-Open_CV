import cv2 as cv
import numpy as np

image=cv.imread('radio.jpg')

canny=cv.Canny(image,125,175)
#cv.imshow('Canny_Pri',canny)

dialet=cv.dilate(canny,(150,150),iterations=65)
#cv.imshow('dialet_pri',dialet)

def translation(image,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(image.shape[1],image.shape[0])

    return cv.warpAffine(image,transMat,dimensions)

#x-->right
#-x-->left
#y-->down
#-y-->top

def rotation(image,angle,rotPoint=None):
    (height,width)=image.shape[:2]

    if rotPoint is None :
        rotPoint=(width//2,height//2)

        rotMat=cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions=(width,height)

        return cv.warpAffine(image,rotMat,dimensions)



translated=translation(dialet,-100,-100)
#cv.imshow('Translated',translated)

rotated=rotation(image,55)
cv.imshow('Rotated',rotated)

rotated_rotated=rotation(rotated,-55)
cv.imshow('skew',rotated_rotated)

resized=cv.resize(image,(200,200),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

flip=cv.flip(image,10)
cv.imshow('flip',flip)

cropped=image[200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)