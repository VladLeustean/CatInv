import random
import pygame as pg
import sys
pg.init ()
WIDTH = 1000
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)
player_size = 50
enemy_size = 50
Smoothie = 0.25
text_1 = "NEW GAME"
text_2 = "QUIT"
Menucolor1 = (102, 165, 171)
Menucolor2 = (206, 192, 163)
font1 = pg.font.SysFont (None, 60)
font2 = pg.font.SysFont (None, 40)
gamefont = pg.font.SysFont ("monospace", 35)

