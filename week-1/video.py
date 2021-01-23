import cv2

vid=cv2.VideoCapture("vtest.avi")

while True:
    success,img=vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
       