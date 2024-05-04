#################
# Import section
#__init__
import pygame as pg
# Key sequences
from keycodes import quit_seq
# Settings
from settings import window_size
################


################
# Objects
pg_display = pg.display
################


def pg_window():
    pg_display.init()
    pg_display.set_mode(window_size)
    pg_display.update()
    pg_watchdog()


def pg_watchdog():
    while True:
        for event in pg.event.get():
            print(event)
            
            if event.type == quit_seq:
                pg.quit()
                return 0
            
        pg_display.flip

if __name__ == '__main__':
    pg_window()