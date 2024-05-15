from ast import main
import copy
from decimal import Decimal
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

x_coords = 0
y_coords = 0    



################

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

#################
# Class Rectangle
class Rectangle:
    def __init__(self, color, x, y):
#        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.width = RECT_SIZE_WIDTH
        self.height = RECT_SIZE_HEIGHT
       
        
#    def __str__(self) -> str:
#        return f'{self.color} rect appears at {self.x},{self.y}. Width {self.width}, Height {self.height}'
        
    def draw(self):
        print (f'{self.color} rect appears at {self.x},{self.y}. Width {self.width}, Height {self.height}')
        return pg.draw.rect(main_surface, self.color, (self.x,self.y, self.width,self.height))




################
# Rect Init
#
blue_block = Rectangle(BLUE, 125, 125)
red_block = copy.deepcopy(blue_block)
red_block.color = RED
red_block.x = 200

red_block.draw()
blue_block.draw()
    
#main_rect = pg.draw.rect(main_surface,BLUE,(x_coords,y_coords,RECT_SIZE_WIDTH, RECT_SIZE_HEIGHT))
###############









def surface_init():    
    draw_screen.blit(main_surface,(0,0))


