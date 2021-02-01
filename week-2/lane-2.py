import cv2
import numpy as np


def canny(lane_img):
     gray_img=cv2.cvtColor(lane_img,cv2.COLOR_RGB2GRAY)
     blur_img=cv2.GaussianBlur(gray_img,(5,5),0)
     canny_img=cv2.Canny(blur_img,50,150)
     return canny_img


def region(lane_img):
     height=lane_img.shape[0]
     poly=np.array([[(860,height),(160,height),(450,300)]])
     mask=np.zeros_like(lane_img)
     cv2.fillPoly(mask,poly,255)
     masked_img=cv2.bitwise_and(lane_img,mask)
     return masked_img

def display_lines(lane_image,lines):
     line_img=np.zeros_like(lane_image)
     if lines is not None:
          for line in lines:
               x1,y1,x2,y2=line.reshape(4)
               cv2.line(line_img,(x1,y1),(x2,y2),(0,0,255),10)
     return line_img


img=cv2.imread('pic2.jpeg')
#image=cv2.resize(img,(462,462))
lane_img=np.copy(img)
canny_img=canny(lane_img)
cropped_image=region(canny_img)
lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
line_img=display_lines(lane_img,lines)
combo=cv2.addWeighted(lane_img,0.8,line_img,1,1)
#cv2.imshow("result",image)
#cv2.imshow("Gray Image",gray_img)
#cv2.imshow("Blurr",blur_img)
#.imshow("Canny",canny_img)
#cv2.imshow("OUTPUT",line_img)
cv2.imshow("resuly",combo)
cv2.waitKey(0)