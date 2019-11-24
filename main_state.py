import random
import json
import os

from pico2d import *
import game_framework
import game_world

from FLOWERS import Sunflower, Peashooter, Wallnut, Sun
from ZOMBIES import Zombie
from GROUND import Ground, UI

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

name = "StartState"
image = None
ui = None

choice = 1
sun_time = 0.0

sflower = []
pflower = []
wflower = []
flowers= [sflower, pflower, wflower]


zombie=[]

sun=[]
bullet=[]

cardcheck = False

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global image, UI

    image = Ground()
    game_world.add_object(image, 0)
    ui = UI()
    game_world.add_object(ui, 0)

def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def update():
    global flower, zombie, sun, sun_time

    if (sun_time > 3.0):
        s = Sun(0, 0)
        sun.append(s)
        game_world.add_object(s,1)
        sun_time = 0
    sun_time += game_framework.frame_time

    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    global ui
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()
    for i in range(9):
        for j in range(5):
            draw_rectangle(50 + 140 * (i), 25 + 100 * j, 50 + 140 * (i + 1), 25 + 100 * (j + 1))

    draw_rectangle(107, 600 - (109 // 2) - 44, 169, 600 - (109 // 2) + 42)
    draw_rectangle(107+ 62 + 11, 600 - (109 // 2) - 44, 169+ 62 + 11, 600 - (109 // 2) + 42)
   # draw_rectangle(50 + 140 * (i), 25 + 100 * j, 50 + 140 * (i + 1), 25 + 100 * (j + 1))
    update_canvas()

def handle_events():
    global choice, sun, sun_count
    global sflower, pflower, wflower
    global cardcheck

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_q:
                choice = 1
            elif event.key == SDLK_w:
                choice = 2
            elif event.key == SDLK_e:
                choice = 3
            elif event.key == SDLK_a:
                choice = 4
            elif event.key ==SDLK_s:
                choice = 5
            elif event.key == SDLK_d:
                choice = 6
            elif event.key == SDLK_z:
                choice = 7

        elif event.type == SDL_MOUSEBUTTONDOWN:
            for i in sun:
                if event.x >= i.x - 39 and event.x <=i.x + 39  \
                    and 600 - event.y >= i.high - 39 and 600 - event.y <= i.high + 39:
                    game_world.remove_object(i)
                    pass

                #self.card.clip_draw(0, 488, 62, 87, 138, 600 - (109 // 2) - 1)
                #self.card.clip_draw(65, 488, 62, 87, 138 + 62 + 11, 600 - (109 // 2) - 1)
                #self.card.clip_draw(195, 488, 62, 87, 138 + 124 + 22, 600 - (109 // 2) - 1)
            if cardcheck == False:
                if event.x > 107 and event.x < 169 and 600- event.y > 600 - (109 // 2) - 44 and 600 - event.y < 600 - (109 // 2) + 42:
                    cardcheck = True
                    choice = 2
                elif event.x > 107+ 62 + 11 and event.x < 169+ 62 + 11 and 600- event.y > 600 - (109 // 2) - 44 and 600 - event.y < 600 - (109 // 2) + 42:
                    cardcheck = True
                    choice = 1
            elif cardcheck == True:
                for i in range(9):
                    for j in range(5):
                        if event.x > (50 + 140 * i) and event.x < (50 + 140 * (i + 1)) \
                                and 600 - event.y > (25 + 100 * j) and 600 - event.y < (25 + 100 * (j + 1)):
                            print("in")
                            if choice == 1:
                                flower = Sunflower((120 + 140 * i), 600 - (75 + 100 * j), sun)
                                sflower.append(flower)
                                game_world.add_object(flower, 1)
                                cardcheck = False
                            elif choice == 2:
                                flower = Peashooter((120 + 140 * i), 600 - (75 + 100 * j))
                                pflower.append(flower)
                                game_world.add_object(flower, 1)
                                cardcheck = False
                            elif choice == 3:
                                wflower.append(Wallnut(event.x, event.y))
                                game_world.add_object(Wallnut(event.x, event.y), 1)
                                cardcheck = False
                            elif choice == 4:
                                zombie.append(Zombie())
                                game_world.add_object(Zombie(), 1)


                    #draw_rectangle(50 + 140 * (i), 25 + 100 * j, 50 + 140 * (i + 1), 25 + 100 * (j + 1))



