import pygame as pg
import sys

pg.init ()

screen = pg.display.set_mode ((800, 600))

playerImg = pg.image.load ("cat.png")
playerX = 370
playerY = 420

def player ():
    screen.blit(playerImg, (playerX, playerY))


game_over = False
while not game_over:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    screen.fill ((0, 0, 0))
    player ()
    pg.display.update ()