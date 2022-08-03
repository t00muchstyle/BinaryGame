import pygame,sys
import random
import time

#Initializing fonts and music
pygame.font.init()
pygame.init()
pygame.mixer.init()

#window width and height

WIDTH, HEIGHT = 600,600
WIN =pygame.display.set_mode((WIDTH,HEIGHT))

#set the caption
pygame.display.set_caption("Binary Game")

#set up speed of the game and frames per second 

FPS = 60
Milliseconds = 60
score = 0 
Time = 120
# the following vaiables help split up the binary numbers and animate
# them on the screen when required

G_1 = False
G_2 = False
G_3 = False
G_4 = False
G_5 = False 
G_6 = False 
G_7 = False 
G_8 = False

#