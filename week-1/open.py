

'''print("Package installed")

#reading a image

img=cv2.imread("lena.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0) '''


#to open webcam
import cv2
cap=cv2.VideoCapture(0)
cap.set(3,840) #for width
cap.set(4,980) #for height
cap.set(10,100) # for brightness

while True:
    sucess, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

