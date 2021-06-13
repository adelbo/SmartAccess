from pirc522 import RFID
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import signal
import time
GPIO.setwarnings(False) 
rc522=RFID()
while True:
    i=0
    code =""
    (error,tag_type)=rc522.request()
    if not error:
        (error,uid)=rc522.anticoll()
        if not error:
            while i < len(uid):
                code +=str(uid[i])
                i+=1
                time.sleep(0.3)
        print(code)
        fichier = open("key.txt","w")
        fichier.write(code)
        fichier.close()
