import cv2 as cv

def resizeScale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('catvid.mp4')

while True:
    istrue,frame=capture.read()
    
    resized_frame=resizeScale(frame,scale=0.2)
    
    resized_frame_1=resizeScale(frame, scale=0.75)


    cv.imshow('video',frame)
    cv.imshow('resizeVide',resized_frame)
    cv.imshow('resized_frame_1',resized_frame_1)
    

    if cv.waitKey(20) & 0xFF == ord('d'):
         break

capture.release()
cv.destroyAllWindows()