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
################

def pg_window(to_draw):
    pg_display.init()
    pg_display.set_mode(window_size)
#    pg_display.update(to_draw)
    pg_display.update()
    pg_watchdog()
    return 0


def pg_watchdog():
    while True:
        for event in pg.event.get():
            print(event)
            
            if event.type == quit_seq:
                pg.quit()
                return 0
        #     
        #pg_display.flip

if __name__ == '__main__':
    pg_window(to_draw=pg_surface)