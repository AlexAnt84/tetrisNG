import pygame as pg
import os

import pygame.event


def pg_window():
    pg_instance = pg.init()
    pg_display = pg.display.set_mode((1024, 768))
    pg.display.update()
    pg_watchdog()


def pg_watchdog():
    while True:
        for event in pygame.event.get():
            print(event)


if __name__ == '__main__':
    pg_window()
