from pyclbr import Class
from main import *
from settings import *
import sys
import pygame as pg

RED = (255,0,0) 
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255, 255, 255)
SCREEN_CENTER = (WINDOW_HEIGHT/2, WINDOW_WIDTH/2)

RECT_SIZE_HEIGHT = 50
RECT_SIZE_WIDTH = 50
#RECT_VALUE = RECT_SIZE_X, RECT_SIZE_Y
    

################
# Objects
draw_screen = pg_display.set_mode(WINDOW_SIZE)
main_surface = pg.Surface(WINDOW_SIZE)
################

################
# Surface param
main_surface.fill(WHITE)
main_surface.set_alpha(200)
################

################
# Rect Init
## TODO Formula
main_rect = pg.draw.rect(main_surface,BLUE,(512,512 + RECT_SIZE_WIDTH,562,RECT_SIZE_WIDTH/2))
###############


    



def surface_init():    
    draw_screen.blit(main_surface,(0,0))


