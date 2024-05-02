#__init__
import pygame as pg
from keycodes import quit_seq as quit_sec


def pg_window():
    pg_instance = pg.init()
    pg_display = pg.display.set_mode((1024, 768))
    pg.display.update()
    pg_watchdog()


def pg_watchdog():
    while True:
        for event in pg.event.get():
            print(event)
            
            if event.type == quit_sec:
                pg.quit()


if __name__ == '__main__':
    pg_window()