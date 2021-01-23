import cv2
import numpy as np

img=cv2.imread("hand-cards-trump-spades.jpg")
print(img.shape)
width,height=450,461
pts1=np.float32([[220,91],[433,135],[164,387],[373,427]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)