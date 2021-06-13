from pirc522 import RFID
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import signal
import time

GPIO.setwarnings(False)
LEDverte =40
LEDrouge = 37 
rc522 = RFID()
buzz=32                                                 
GPIO.setup(buzz,GPIO.OUT)
GPIO.setup(LEDverte,GPIO.OUT)
GPIO.setup(LEDrouge,GPIO.OUT)
GPIO.output(LEDverte,GPIO.LOW)
GPIO.output(LEDrouge,GPIO.LOW)
GPIO.output(buzz,GPIO.LOW)
while True:
     GPIO.output(LEDverte,GPIO.LOW)
     GPIO.output(LEDrouge,GPIO.LOW)
     GPIO.output(buzz,GPIO.LOW)
     i=0
     code=""
      
     
     (error, tag_type) = rc522.request()
     if not error:
        (error, uid) = rc522.anticoll()
        if not error:
            for i in range(0, len(uid)):
                code += str(uid[i])
                time.sleep(0.05)
   
            print(code)
            fichier = open("key.txt","w")
            fichier.write(code)
            fichier.close()
            if(code=="43100103411"):
                 GPIO.output(buzz,GPIO.HIGH)
                 GPIO.output(LEDverte,GPIO.HIGH)
                 time.sleep(1)
                 GPIO.output(buzz,GPIO.LOW)
                 GPIO.output(LEDverte,GPIO.LOW)
            elif(code=="1056436163174"):
                 GPIO.output(buzz,GPIO.HIGH)
                 GPIO.output(LEDverte,GPIO.HIGH)
                 time.sleep(1)
                 GPIO.output(buzz,GPIO.LOW)
                 GPIO.output(LEDverte,GPIO.LOW)
            
            else:
                 GPIO.output(LEDrouge,GPIO.HIGH)
                 time.sleep(1)
                 GPIO.output(buzz,GPIO.LOW)
                 GPIO.output(LEDrouge,GPIO.LOW)
    
    
    
          
