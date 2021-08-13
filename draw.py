import cv2  as cv 
import numpy as np

def scaleResize(frame,scale=0.75):
    width=frame.shape[0]*scale
    height=frame.shape[1]*scale
    dimensions=(width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)

blank[:]=100,200,255
#cv.imshow('Green',blank)

blank[200:300,200:300]=255,255,255
#cv.imshow('faka',blank)

cv.rectangle(blank,(0,0),(200,200),(0,255,0),thickness=2)
#cv.imshow('meaw',blank)

cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),20,(255,0,0),thickness=5)
#cv.imshow('Circle',blank)

cv.line(blank,(0,0),(blank.shape[1]//2+10,blank.shape[0]//2+10),(0,255,100),thickness=10)
#cv.imshow('Line',blank)

cv.putText(blank,'Smol Kitty...',(100,100),cv.FONT_HERSHEY_TRIPLEX,2.0,(0,0,0),thickness=1)
#cv.imshow('MyText1',blank)


#real image
image=cv.imread('cat.jpg')
#cv.imshow('Cat',image)

cv.rectangle(image,(100,100),(450,450),(0,255,0),thickness=2)
#cv.imshow('identify',image)

cv.rectangle(image,(0,0),(image.shape[1]//2,image.shape[0]//2),(0,250,0),thickness=cv.FILLED)
#cv.imshow('Hey',image)

cv.circle(image,(image.shape[0]//2,image.shape[1]//2),100,(0,0,255),thickness=10)
#cv.imshow('circle1',image)

cv.putText(image,'Smol Kitty...',(100,100),cv.FONT_HERSHEY_TRIPLEX,2.0,(0,0,0),thickness=1)
#cv.imshow('MyText',image)

cv.putText(image,'meaw meaw ',(image.shape[1]//3,image.shape[0]//3),cv.FONT_HERSHEY_SIMPLEX,2.0,(0,250,0),thickness=3)
#cv.imshow('myText2',image)

gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

rgb=cv.cvtColor(image,cv.COLOR_BGR2LAB)
#cv.imshow('RGB',rgb)

#blur

blur=cv.blur(image,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

gauss=cv.GaussianBlur(image,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('Gaussian',gauss)

#canny

canny=cv.Canny(image,125,175)
#cv.imshow('Canny Pic',canny)

rover=cv.imread('rover.jpg')
#cv.imshow('ROver',rover)

pia=cv.imread('pia.jpg')

canny_2=cv.Canny(pia,125,175)
cv.imshow('Pia',canny_2)

dilate=cv.dilate(canny_2,(65,65),iterations=20)
cv.imshow('Pia Dilate',dilate)


canny_1=cv.Canny(rover,125,175)
#cv.imshow('canny_1',canny_1)

eroded=cv.erode(dilate,(7,7),iterations=6)
cv.imshow('Eroded',eroded)

#resize

resi=cv.resize(pia,(200,200))
cv.imshow('Resized',resi)

#croping

crop=pia[50:200,200:400]
cv.imshow('Croppd',crop)

cv.waitKey(0)