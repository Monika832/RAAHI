import cv2
import numpy as np

img=np.zeros((640,640,3),np.uint8)
img2=np.zeros((640,640,3),np.uint8)

#print(img)

#for line
img2[:]=0,255,0
#cv2.line(img,(10,100),(210,400),(0,0,255),3)
#cv2.rectangle(img2,(10,100),(210,400),(0,0,255),3)
cv2.rectangle(img2,(100,100),(210,400),(0,0,255),cv2.FILLED)
cv2.circle(img2,(400,500),50,(0,255,255),cv2.FILLED)
cv2.putText(img2,"....OPENCV....",(250,100),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,0,255),2)


#cv2.line(img,(100,50),(img.shape[2],img.shape[0]),(0,255,0),3)
cv2.imshow("Image",img2)

cv2.waitKey(0)