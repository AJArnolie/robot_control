import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((200,200))

while(True):
    e = pygame.event.get()
    print(e)
    for event in e:
        print(2000000)
        if (event.type == KEYDOWN):
            print(3000000000000000)
            if (event.key == K_0):
                print "numpad 0"
            if (event.key == K_1):
                print "numpad 1"
