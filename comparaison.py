import cv2
import numpy as np
from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec=cv2.createLBPHFaceRecognizer()
rec.load('train/trainner.yml')
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
code=""
LEDverte = 40 
LEDrouge = 12
buzz=26
GPIO.setup(buzz,GPIO.OUT)
GPIO.setup(LEDverte,GPIO.OUT)
GPIO.setup(LEDrouge,GPIO.OUT)
GPIO.output(LEDverte,GPIO.LOW)
GPIO.output(LEDrouge,GPIO.LOW)
GPIO.output(buzz,GPIO.LOW)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    img = frame.array
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = rec.predict(gray[y:y+h,x:x+w])
        if (Id==1):
            Id="Adel"
            code="43100103411"
            GPIO.output(buzz,GPIO.HIGH)
            GPIO.output(LEDverte,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(buzz,GPIO.LOW)
            GPIO.output(LEDverte,GPIO.LOW)
            fichier = open("file.txt","w")
            fichier.write(code)
            fichier.close()
        elif (Id==2):
            Id="hiba"
            code="1056436163174"
            GPIO.output(buzz,GPIO.HIGH)
            GPIO.output(LEDverte,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(buzz,GPIO.LOW)
            GPIO.output(LEDverte,GPIO.LOW)
            fichier = open("file.txt","w")
            fichier.write(code)
            fichier.close()
        else:
            Id="inconnue"
        
        cv2.cv.PutText(cv2.cv.fromarray(img),str(Id), (x,y+h),font, 255) 
    cv2.imshow('frame',img);
    rawCapture.truncate(0)
    if(cv2.waitKey(1)==ord('q')):
        break;
    
cam.release()
cv2.destroyAllWindows()
