import cv2
 
       
vc = cv2.VideoCapture('./images/surfVideo.mp4') 
c=1
 
if vc.isOpened(): 
    rval , frame = vc.read()
else:
    rval = False
 
timeF = 24  
 
while rval: 
    rval, frame = vc.read()
    if(c%timeF == 0):
        cv2.imwrite('./images/train/'+str(c) + '.jpg',frame)
    c = c + 1
    cv2.waitKey(1)
vc.release()
