import game_framework
#import title_state
from pico2d import *
import sunflower
import zombie
import random

name = "StartState"
image = None
UI = None
sun_time = 0.0

choice=0
flower=[]
sun=[]
ombie=[]
bullet=[]

def enter():
    global image, UI , ombie
    image = load_image('Tutorial_map.png')
    UI = load_image('board.png')
    ombie.append(zombie.Zombie())


def exit():
    global image, UI
    del(image)
    del(UI)



def update():
    global sun_time, sun, zombie
    for i in flower:
        i.shoot(bullet)
    for i in bullet:
        i.move()
    #for i in flower:
   #     i.makeSun(sun)

    #if (sun_time > 1.0):
        #sun.append(sunflower.Sun())
        #sun_time = 0
    for i in ombie:
        i.move()
    delay(0.01)
    #sun_time += 0.01
    pass

def draw():
    global image ,UI
    clear_canvas()
    image.clip_draw(225 , 0, 800, 600, 700, 300, 1400, 600)
    UI.clip_draw(0,0,557,109,(557//2),600-(109//2))

    #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    for i in flower:
        i.draw()
    for i in sun:
        i.draw()
    for i in ombie:
        i.draw()
    for i in bullet:
        i.draw()
    update_canvas()


def handle_events():
    global choice
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_MOUSEBUTTONDOWN:
            flower.append(sunflower.Peashooter(event.x, event.y))
            #flower.append(sunflower.Sunflower(event.x, event.y))


def pause(): pass


def resume(): pass
