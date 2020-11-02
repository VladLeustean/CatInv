import pygame as pg
import random
import sys
import Variables as Var
import KittyGame


pg.init ()
GameSpeed = 10
pg.display.set_caption ('game base')
screen = pg.display.set_mode ((Var.WIDTH, Var.HEIGHT), 0, 32)
mainClock = pg.time.Clock ()

DIFFICULTY = (10, "LOW")

music = pg.mixer.music.load ('Backmusic.mp3')
pg.mixer.music.play(-1)


def draw_text (text, font, color, surface, x, y):
    textobj = font.render (text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit (textobj, textrect)

def options ():
    running = True
    while running:
        screen.fill (Var.BACKGROUND_COLOR)
        draw_text('Options', Var.font1, Var.BLUE, screen, 360, 20)
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                pg.quit ()
                sys.exit ()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
        pg.display.update ()
        mainClock.tick (60)

def kittyscore (KittyListUpdated):
    running = True
    while running:
        screen.fill (Var.BACKGROUND_COLOR)
        draw_text ('KittyGame Highscore', Var.font1, Var.BLUE, screen, 320, 20)
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                pg.quit ()
                sys.exit ()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
        for i in range (1, 11):
            ypos = 50 + i*50
            draw_text ("{} _ _ _ _ _ _ _ _ _ _".format (i), Var.font2, Var.YELLOW, screen, 150, ypos)
            draw_text("{}".format (KittyListUpdated[i-1]), Var.font2, Var.YELLOW, screen, 450, ypos)
        pg.display.update ()
        mainClock.tick (60)


def highscore (KittyListUpdated):
    running = True
    click = False
    while running:
        button_1 = pg.Rect (120, 120, 300, 200)
        screen.fill (Var.BACKGROUND_COLOR)
        draw_text ('Highscores', Var.font1, Var.BLUE, screen, 360, 20)
        mx, my = pg.mouse.get_pos ()
        
        if button_1.collidepoint ((mx, my)):
            if click:
                kittyscore(KittyListUpdated)
        click = False

        for event in pg.event.get ():
            if event.type == pg.QUIT:
                pg.quit ()
                sys.exit ()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pg.draw.rect (screen, Var.Menucolor1, button_1)
        draw_text ("KITTYGAME", Var.font2, Var.Menucolor2, screen, 170, 200)
        pg.display.update ()
        mainClock.tick (60)

def play (DIFFICULTY, KittyList):
    running = True
    click = False
    KITTYHIGHSCORE = KittyList [0]
    while running:
        screen.fill (Var.BACKGROUND_COLOR)
        draw_text('Games', Var.font1, Var.BLUE, screen, 360, 20)
        button_1 = pg.Rect (120, 120, 300, 200)
        mx, my = pg.mouse.get_pos ()
        

        if button_1.collidepoint ((mx, my)):
            if click:
                NEWSCORE = KittyGame.start_game (DIFFICULTY [0], KITTYHIGHSCORE)
                if NEWSCORE > min (KittyList[0:10]):
                    for i in range (10):
                        if KittyList [i] < NEWSCORE:
                            KittyList = KittyList [0:i] + [NEWSCORE] + KittyList [i:]
                            print (KittyList)
                            break
                KITTYHIGHSCORE = KittyList [0]

        click = False
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                pg.quit ()
                sys.exit ()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pg.draw.rect (screen, Var.Menucolor1, button_1)
        draw_text ("KITTYGAME", Var.font2, Var.Menucolor2, screen, 170, 200)
        pg.display.update ()
        mainClock.tick (60)
    return KittyList


def menu ():
    KittyList = [0] * 10
    KittyListUpdated = [0] * 10
    click = False
    while True:
        screen.fill(Var.BACKGROUND_COLOR)
        draw_text('Main Menu', Var.font1, Var.BLUE, screen, 360, 20)

        mx, my = pg.mouse.get_pos ()

        button_1 = pg.Rect (370, 150, 200, 50)
        button_2 = pg.Rect (370, 250, 200, 50)
        button_3 = pg.Rect (370, 350, 200, 50)
        button_4 = pg.Rect (370, 450, 200, 50)

        if button_1.collidepoint ((mx, my)):
            if click:
                KittyListUpdated = play (DIFFICULTY, KittyList)
        if button_2.collidepoint ((mx, my)):
            if click:
                options ()
        if button_3.collidepoint ((mx, my)):
            if click:
                highscore (KittyListUpdated)
        if button_4.collidepoint ((mx, my)):
            if click:
                pg.quit()
                sys.exit()
        click = False
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                pg.quit ()
                sys.exit ()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit ()
                    sys.exit ()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
            pg.draw.rect (screen, Var.Menucolor1, button_1)
            pg.draw.rect (screen, Var.Menucolor1, button_2)
            pg.draw.rect (screen, Var.Menucolor1, button_3)
            pg.draw.rect (screen, Var.Menucolor1, button_4)
            draw_text('Play', Var.font2, Var.Menucolor2, screen, 440, 160)
            draw_text('Options', Var.font2, Var.Menucolor2, screen, 420, 260)
            draw_text('Highscore', Var.font2, Var.Menucolor2, screen, 400, 360)
            draw_text('Exit', Var.font2, Var.Menucolor2, screen, 440, 460)
            draw_text('DIFFICULTY: {}'.format(DIFFICULTY [1]), Var.font2, Var.Menucolor2, screen, 700, 520)

            pg.display.update ()
            mainClock.tick (60)
            KittyList = KittyListUpdated
   
menu ()
