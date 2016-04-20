import sys
import time
import pygame
import pygame.camera
from pygame.locals import *
import RPi.GPIO as GPIO

RR = 20
RF = 24
LF = 16
LR = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RF,GPIO.OUT)
GPIO.setup(RR,GPIO.OUT)
GPIO.setup(LF,GPIO.OUT)
GPIO.setup(LR,GPIO.OUT)

GPIO.output(RF,False)
GPIO.output(RR ,False)
GPIO.output(LF,False)
GPIO.output(LR ,False)


pygame.init()
screen = pygame.display.set_mode((50, 50))
pygame.mouse.set_visible(0)

pygame.display.set_caption('PIBOT')
pygame.mouse.set_visible(4)

done = False
while not done:

    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == (K_UP):
    
                GPIO.output(RF,True)
                GPIO.output(LF,True)
                GPIO.output(RR ,False)
                GPIO.output(LR,False)

            if event.key == (K_DOWN):
    
                GPIO.output(RF,False)
                GPIO.output(LF,False)
                GPIO.output(RR ,True)
                GPIO.output(LR,True)

            if event.key == (K_LEFT):
    
                GPIO.output(RF,True)
                GPIO.output(RR,False)
                GPIO.output(LR,True)
                GPIO.output(LF,False)

            if event.key == (K_RIGHT):
    
                GPIO.output(RR,True)
                GPIO.output(LF,True)
                GPIO.output(LR,False)
                GPIO.output(RF,False)

        if event.type == KEYUP:

            if event.key == (K_UP):

                GPIO.output(RR,False)
                GPIO.output(RF,False)
                GPIO.output(LF ,False)
                GPIO.output(LR,False)

            if event.key == (K_DOWN):

                GPIO.output(RR,False)
                GPIO.output(RF,False)
                GPIO.output(LF ,False)
                GPIO.output(LR,False)

            if event.key == (K_LEFT):
    
                GPIO.output(RR,False)
                GPIO.output(RF,False)
                GPIO.output(LF ,False)
                GPIO.output(LR,False)
                
            if event.key == (K_RIGHT):
    
                GPIO.output(RR,False)
                GPIO.output(RF,False)
                GPIO.output(LF ,False)
                GPIO.output(LR,False)
                 
            if event.key == (K_ESCAPE):
                GPIO.cleanup()
                done = True
