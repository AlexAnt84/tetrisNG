from ast import main
import copy
from decimal import Decimal
from pyclbr import Class
from typing import Self
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
# Class Rectangle. Prototype Pattern
class Rectangle:
    def __init__(self, color, pos_x, pos_y):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = RECT_SIZE_WIDTH
        self.height = RECT_SIZE_HEIGHT
        

        
    def draw(self):
        print (f'NEW {self.color} rect appears at {self.x},{self.y}. Width {self.width}, Height {self.height}')
        return pg.draw.rect(main_surface, self.color, (self.x,self.y, self.width,self.height))

#################
# Class Tetramino
class Tetramino:
    def __init__ (self, tetramino, color, pos_x, pos_y):
        
        block_prototype = Rectangle(self.color,self.pos_x, self.pos_y)
        
        match self.tetramino:
            case self.I: 
                l_block_1 = copy.deepcopy(block_prototype)
                l_block_2 = copy.deepcopy(block_prototype)
                l_block_3 = copy.deepcopy(block_prototype)
                l_block_4 = copy.deepcopy(block_prototype)
                                
                #######
                #    
                # 1 X  
                # 2 X
                # 3 X
                # 4 X   
                #   
                #######
                
                l_blocks = list()
                
                for i in range(1,4):
                    l_blocks.append("l_block_" + i)
                
                print (l_blocks)
                   
            case self.J:
                #######
                # 
                #   X
                #   X
                #  XX
                #
                #######
                pass
            
            case self.L:
                #######
                #
                #
                #  X
                #  X
                #  XX
                #
                ########
                pass
                    
            case self.O:
                #######
                #
                #
                #  XX
                #  XX
                #
                #######
                pass    
                
            case self.S:
                #######
                #
                #
                #  XX
                # XX
                #    
                #######
                pass
            
            case self.T:
                #######
                #
                #
                # XXX
                #  X
                # 
                #######
                pass
                
            case self.Z:
                #######
                #
                #
                # XX
                #  XX
                # 
                #######
                pass
         


        


################
# Testing purposes
#
block_prototype = Rectangle(BLUE, 125, 125)


red_block = copy.deepcopy(block_prototype)
red_block.color = RED
red_block.x = 200

red_block.draw()
block_prototype.draw()
    
###############









def surface_init():    
    draw_screen.blit(main_surface,(0,0))


