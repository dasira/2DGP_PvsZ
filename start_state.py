import game_framework
import main_state
from pico2d import *
import sunflower

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('main_image.png')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(main_state)
    delay(0.01)
    logo_time += 0.01
    pass

def draw():
    global image
    clear_canvas()
    image.draw(700,300,1400,600)

    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def pause(): pass


def resume(): pass
