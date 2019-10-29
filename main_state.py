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
money = 0
moveS = 0
choice = 1


sflower = []
pflower = []
wflower = []
flower= [sflower, pflower, wflower]

sun=[]
Zombie=[]
bullet=[]

def enter():
    global image, UI
    image = load_image('Tutorial_map.png')
    UI = load_image('board.png')


def exit():
    global image, UI
    del(image)
    del(UI)


def update():
    global sun_time, sun, bullet, moveS
    for i in pflower:
        for j in Zombie:
            if j.y <= 400 and j.y>= 250:
                i.shootS = 1
            else:
                i.shootS = 0
        if i.shootS == 1:
            i.shoot(bullet)
    for i in bullet:
        i.move()
    for i in sun:
        i.update()

    for i in sflower:
        i.makeSun(sun)
    for i in Zombie:
        for j in flower:
            for w in j:
                if w.x >= i.x:
                    i.moveS = 1

        if i.moveS == 0:
            i.move()
        else:
            for j in flower:
                for w in j:
                    if (i.Atime > 1.0):
                        w.HP -= i.damage
                        i.Atime = 0
                        if w.HP <= 0:
                            j.remove(w)
                            i.moveS = 0
            i.Atime += 0.01

    for i in Zombie:
        for j in bullet:
            if j.x + 28 >= i.x:
                i.HP -= 1
                bullet.remove(j)
                if i.HP == 0:
                    Zombie.remove(i)

    if (sun_time > 3.0):
        sun.append(sunflower.Sun(0,0))
        sun_time = 0
    delay(0.01)
    sun_time += 0.01
    pass

def draw():
    global image ,UI
    clear_canvas()
    image.clip_draw(225 , 0, 800, 600, 700, 300, 1400, 600)
    UI.clip_draw(0,0,557,109,(557//2),600-(109//2))

    # 9  5
    # 1260 500
    for i in range(9):
        for j in range(5):
            draw_rectangle(50+ 140*(i), 25+ 100*j, 50+ 140*(i+1), 25+ 100*(j+1))
    for i in flower:
        for j in i:
            j.draw()
    for i in Zombie:
        i.draw()
    for i in sun:
        i.draw()
    for i in bullet:
        i.draw()
    #draw_rectangle(50, 25, 1310, 525)

    update_canvas()


def handle_events():
    global choice, sun, sun_count
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
        elif event.type == SDL_MOUSEBUTTONDOWN:
            for i in sun:
                if event.x >= i.x - 39 and event.x <=i.x + 39  \
                    and 600 - event.y >= i.high - 39 and 600 - event.y <= i.high + 39:
                    sun.remove(i)
            if choice == 1:
                sflower.append(sunflower.Sunflower(event.x, event.y))
            elif choice == 2:
                pflower.append(sunflower.Peashooter(event.x, event.y))
            elif choice == 3:
                wflower.append(sunflower.Wallnut(event.x, event.y))
            elif choice == 4:
                Zombie.append(zombie.Zombie())
            elif choice == 5:
                Zombie.append(zombie.CheadZombie())
            elif choice == 6:
                Zombie.append(zombie.BheadZombie())


def pause(): pass


def resume(): pass
