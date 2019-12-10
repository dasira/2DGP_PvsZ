from pico2d import *
import game_framework
import game_world
import pause_state

from stage import stage01

name = "Stage"

Stage = None


def enter():
    game_world.objects = [[], []]

    global Stage
    Stage = stage01()
    game_world.add_object(Stage, 0)

def exit():
    game_world.clear()

def pause():
    pass
def resume():
    pass
def handle_events():
    global Stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:

            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:

            game_framework.push_state(pause_state)
        else :
            Stage.handle_event(event)
    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()