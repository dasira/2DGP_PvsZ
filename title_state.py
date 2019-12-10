import game_framework
import game_world
from pico2d import *
import stage_state


name = "Title"
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

    pass

def draw():
    global image
    clear_canvas()
    image.draw(700,300,1400,600)
    menu.clip_draw(0, 150, 620, 150,700, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.x >= 390 and event.x <= 1010 and 600 - event.y >= 250 and 600 - event.y <= 375:
                game_framework.change_state(stage_state)


def pause(): pass


def resume(): pass
