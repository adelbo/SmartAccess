import face_recognition
import picamera
import numpy as np
import RPi.GPIO as GPIO
import signal
import time
from espeak import espeak
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
fichier=open("file.txt","w")
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)
code=""
LEDverte = 38 
LEDrouge = 37
buzzer=32

print("Reconnaissance faciale en cours ...")
adel_image = face_recognition.load_image_file("me.jpg")
adel_face_encoding = face_recognition.face_encodings(adel_image)[0]

hiba_image = face_recognition.load_image_file("hiba.jpg")
hiba_face_encoding = face_recognition.face_encodings(hiba_image)[0]


# Initialize some variables
face_locations = []
face_encodings = []

while True:
    GPIO.setup(buzzer,GPIO.OUT)
    GPIO.setup(LEDverte,GPIO.OUT)
    GPIO.setup(LEDrouge,GPIO.OUT)
    GPIO.output(LEDverte,GPIO.LOW)
    GPIO.output(LEDrouge,GPIO.LOW)
    GPIO.output(buzzer,GPIO.LOW)
    print("capture de la photo en cours...")
    camera.capture(output, format="rgb")
    face_locations = face_recognition.face_locations(output)
    print("il y a {} visage (s) dans l'image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)
   
    for face_encoding in face_encodings:
       
        match = face_recognition.compare_faces([adel_face_encoding], face_encoding)
        match2 = face_recognition.compare_faces([hiba_face_encoding], face_encoding)

        name = "Inconnue"
        code="210"
        GPIO.output(LEDrouge,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LEDrouge,GPIO.LOW)

        if match[0]:
            GPIO.output(LEDrouge,GPIO.LOW)
            name = "adel"
            code="20816862167225"
            GPIO.output(LEDrouge,GPIO.LOW)
            GPIO.output(buzzer,GPIO.HIGH)
            GPIO.output(LEDverte,GPIO.HIGH)
            espeak.synth ("Welcome")
            time.sleep(1)
            GPIO.output(LEDrouge,GPIO.LOW)
            GPIO.output(buzzer,GPIO.LOW)
            GPIO.output(LEDverte,GPIO.LOW)

        if match2[0]:
            name = "hiba"
            code="43100103411"
            GPIO.output(LEDrouge,GPIO.LOW)
            GPIO.output(buzzer,GPIO.HIGH)
            GPIO.output(LEDverte,GPIO.HIGH)
            espeak.synth ("Welcome")
            time.sleep(1)
            GPIO.output(LEDrouge,GPIO.LOW)
            GPIO.output(buzzer,GPIO.LOW)
            GPIO.output(LEDverte,GPIO.LOW)


        print("le visage dans la photo est de  {}!".format(name))
   
        print (code)
        fichier = open("file.txt","w")
        fichier.write(code)
        fichier.close()
