import game_framework
import main_state
from pico2d import *
import FLOWERS

name = "StartState"
image = None
menu = None
logo_time = 0.0


def enter():
    global image, menu
    image = load_image('main_image.png')
    menu = load_image('Select_Stage.png')


def exit():
    global image
    del(image)


def update():
        #game_framework.change_state(main_state)

    pass

def draw():
    global image
    clear_canvas()
    image.draw(700,300,1400,600)
    menu.draw(700,300)
    draw_rectangle(390, 25, 1010, 150)
    draw_rectangle(390, 195, 1010, 320)
    draw_rectangle(390, 367, 1010, 492)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.x >= 390 and event.x <= 1010 and 600 - event.y >= 367 and 600 - event.y <= 492:
                game_framework.change_state(main_state)
            elif event.x >= 390 and event.x <= 1010 and 600 - event.y >= 25 and 600 - event.y <= 150:
                game_framework.quit()

def pause(): pass


def resume(): pass
