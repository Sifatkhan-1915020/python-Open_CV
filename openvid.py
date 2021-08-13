import cv2 as cv

def resizeScale(frame,scale=0.75):

    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(height,width)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)





capture=cv.VideoCapture('catvid.mp4')

while True:
    istrue,frame=capture.read()
    resized_frame=resizeScale(frame,scale=0.4)
    cv.imshow("Kitty",frame)
    cv.imshow("New Kitty",resized_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
