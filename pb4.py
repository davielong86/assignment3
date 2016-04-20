import sys
from time import sleep
import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
#create fullscreen display 640x480
screen = pygame.display.set_mode((800,600),0)

#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(32,24))
webcam.start()

pygame.display.set_caption('PIBOT')
pygame.mouse.set_visible(4)

done = False
while not done:

    #grab image, scale and blit to screen
    imagen = webcam.get_image()
    imagen = pygame.transform.scale(imagen,(1080,920))
    screen.blit(imagen,(0,0))

    #draw all updates to display
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == (K_ESCAPE):
                done = True
