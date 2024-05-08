#################
# Import section
#__init__
import pygame as pg
# Graphics
from graphics import *
# Key sequences
from keycodes import *
# Settings
from settings import *
################


################
# Objects
pg_display = pg.display

#draw_screen = pg.Surface(window_size)
################

def pg_window():
    pg_display.init()
    pg_display.set_mode(window_size)
    surface_init()
    pg_display.update()
    pg_watchdog()
    return 0


def pg_watchdog():
    while True:
        
        for event in pg.event.get():
            print(event)
            
            if event.type == quit_seq:
                sys.exit()
        
        pg.time.delay(10)


if __name__ == '__main__':
    pg_window()