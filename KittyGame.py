import pygame as pg
import random
import sys
import Variables as Var


pg.init ()
screen = pg.display.set_mode ((Var.WIDTH, Var.HEIGHT))
clock = pg.time.Clock ()

playerImg = pg.image.load ('kittie.png')
myFont = pg.font.SysFont ("monospace", 35)

def start_game (SPEED, HIGHSCORE):
    pg.event.clear()
    game_over = False
    x = 0
    y = 0
    enemy_position = [random.randint (0, Var.WIDTH - Var.enemy_size), 0]
    enemy_list = [enemy_position]
    SCORE = 0
    player_position = [Var.WIDTH/2, Var.HEIGHT/5*4]
    
    while not game_over:

        screen.fill(Var.BACKGROUND_COLOR)

        for event in pg.event.get():

            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                x = player_position [0]
                y = player_position [1]
                if event.key == pg.K_LEFT and x - Var.player_size > 0-Var.player_size/2:
                    x -= Var.player_size
                elif event.key == pg.K_RIGHT and x + Var.player_size < Var.WIDTH:
                    x += Var.player_size
                #elif event.key == pg.K_UP and y - Var.player_size > Var.HEIGHT/2:
                    #y -= Var.player_size
                #elif event.key == pg.K_DOWN and y + Var.player_size < Var.HEIGHT-Var.player_size/2:
                    #y += Var.player_size
                player_position = [x, y]

        if collision_check (enemy_list, enemy_position, player_position) == 1:
            game_over = True
            break

        draw_enemies (enemy_list, enemy_position)
        drop_enemies (enemy_list)
        SCORE = update_enemy_positions (enemy_list, SCORE, SPEED, enemy_position)
        player_draw (playerImg, player_position)
        draw_text ("Score: {}".format(SCORE), Var.gamefont, Var.YELLOW, screen, Var.WIDTH - 250, Var.HEIGHT - 40)
        draw_text ("HIGHSCORE: {}".format(HIGHSCORE), Var.gamefont, Var.YELLOW, screen, Var.WIDTH - 340, Var.HEIGHT - 100)
        #pg.draw.rect (screen, Var.RED, (player_position [0], player_position[1], Var.player_size, Var.player_size))
        clock.tick(20)
        if SPEED < 15:
            SPEED += 0.1
        pg.display.update()
    Congrats (SCORE)
    return SCORE

def Congrats (SCORE):
    running = True
    while running:
        screen.fill (Var.BACKGROUND_COLOR)
        draw_text('Congratulations!', Var.font1, Var.BLUE, screen, 320, 20)
        draw_text("Your score is: {}".format (SCORE), Var.font2, Var.Menucolor2, screen, 360, 150)
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                pg.quit ()
                sys.exit ()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
        pg.display.update ()



def player_draw (playerImg, player_position):
    screen.blit (playerImg, player_position)


def detect_collision2 (player_position, enemy_position):
    p_x = player_position [0]
    p_y = player_position [1]
    e_x = enemy_position [0]
    e_y = enemy_position [1]
    if abs (p_x - e_x) < Var.player_size and abs (p_y - e_y) < Var.player_size:
        return 1
    return 0

def drop_enemies (enemy_list):
    delay = random.random()
    if len (enemy_list) < 10 and delay < Var.Smoothie:
        x_pos = random.randint (0, Var.WIDTH - Var.enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies (enemy_list, enemy_position):
    for enemy_position in enemy_list:
        pg.draw.rect (screen, Var.BLUE, (enemy_position [0], enemy_position[1], Var.enemy_size, Var.enemy_size))

def update_enemy_positions (enemy_list, SCORE, SPEED, enemy_position):
    for index, enemy_position in enumerate (enemy_list):
        if enemy_position[1] >= 0 and enemy_position [1] < Var.HEIGHT:
            enemy_position[1] += SPEED
        else:
            enemy_list.pop(index)
            SCORE += 10
    return SCORE

def collision_check (enemy_list, enemy_position, player_position):
    for enemy_position in enemy_list:
        if detect_collision2 (enemy_position, player_position):
            return True
    return False

def draw_text (text, font, color, surface, x, y):
    textobj = font.render (text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit (textobj, textrect)