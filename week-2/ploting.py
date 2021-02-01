import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny(lane_img):
     gray_img=cv2.cvtColor(lane_img,cv2.COLOR_RGB2GRAY)
     blur_img=cv2.GaussianBlur(gray_img,(5,5),0)
     canny_img=cv2.Canny(blur_img,50,150)
     return canny_img


img=cv2.imread('test_image.jpg')
print(img.shape)
#image=cv2.resize(img,(462,462))
lane_img=np.copy(img)
canny_img=canny(lane_img)

plt.imshow(img)
plt.show( )