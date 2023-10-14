import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)

GPIO.output(5,True)
time.sleep(5)
GPIO.output(5,False)



