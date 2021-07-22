import time
import cv2

print("CV2 Version %s" %(cv2.__version__))

#cap = cv2.VideoCapture('rtsp://192.168.1.237:8554/server')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Video port not opened!")
else:
    print("Video port is open")

while True:
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cap.release()
