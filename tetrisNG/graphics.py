from main import *
from settings import *
import sys
import pygame as pg

RED = (255,0,0) 
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255, 255, 255)
#rect_size_x = 0,10
#rect_size_y = 0,10
    

################
# Objects
draw_screen = pg_display.set_mode(window_size)
main_surface = pg.Surface(window_size)
################

################
# Surface param
main_surface.fill(WHITE)
main_surface.set_alpha(200)
################


def surface_init():    
    draw_screen.blit(main_surface,(0,0))
    



