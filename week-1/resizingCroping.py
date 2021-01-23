import cv2

img=cv2.imread("tree.png")
print(img.shape)

ResizeImg=cv2.resize(img,(640,480))
imgCropped=img[100:150,200:500]
print(imgCropped.shape)

cv2.imshow("Image",img)
cv2.imshow(" Resize Image",ResizeImg)
cv2.imshow("Cropped img",imgCropped)


cv2.waitKey(0)