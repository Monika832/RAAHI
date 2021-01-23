import cv2
import numpy as np

img=cv2.imread("lena.jpg")
kernel= np.ones((5,5),np.uint8)

#imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#imgBlur =cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(img,100,100) # to find edges in image
imgDilation=cv2.dilate(imgCanny,kernel,iterations=5)
imgErode=cv2.erode(imgDilation,kernel,iterations=1)
imgErode2=cv2.erode(img,kernel,iterations=1)



#cv2.imshow("Gray Image", imgGray)
#cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialate Image", imgDilation)
cv2.imshow("Eroded Image",imgErode)
cv2.imshow("Eroded2 Image",imgErode2)



cv2.waitKey(0)