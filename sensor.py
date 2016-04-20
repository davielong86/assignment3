import sys
import time
import RPi.GPIO as GPIO

TRIG1 = 6
ECHO1 = 19
TRIG2 = 18
ECHO2 = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)


while 1:
    GPIO.output(TRIG1, False)
    time.sleep(1)
    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)
    while GPIO.input(ECHO1)==0:
        pulse_start1 = time.time()
    while GPIO.input(ECHO1)==1:
        pulse_end1 = time.time() 
    GPIO.output(TRIG2, False)
    time.sleep(1)
    GPIO.output(TRIG2, True)
    time.sleep(0.00001)
    GPIO.output(TRIG2, False)
    while GPIO.input(ECHO2)==0:
        pulse_start2 = time.time()
    while GPIO.input(ECHO2)==1:
        pulse_end2 = time.time() 


    pulse_duration1 = pulse_end1 - pulse_start1
    pulse_duration2 = pulse_end2 - pulse_start2

    distanceR = (pulse_duration1 * 17150)
    distanceR = round(distanceR,2)
    distanceL = (pulse_duration2 * 17150) + 250
    distanceL = round(distanceL,2)

    print ("Right:",(distanceR),"cm","Left:",(distanceL),"cm")
