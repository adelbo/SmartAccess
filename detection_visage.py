import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('face',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    rawCapture.truncate(0)
cap.release()
cv2.destroyAllWindows()
 
