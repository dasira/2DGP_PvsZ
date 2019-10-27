from pico2d import *
import random

#숫자 줘서 구분합시다

class Sunflower:
    def __init__(self,x,y):
        self.x,self.y = x, 600-y
        self.image = load_image('SunFlower_0.png')
        self.time=0.0
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x,self.y)

    def makeSun(self,sun):
        if self.time > 10:
            sun.append(Sun())
            self.time=0.0

        self.time+=0.1
        pass


class Sun:
    def __init__(self):
        self.x, self.y = random.randint(100,700), random.randint(100,500)
        self.image = load_image('Sun_0.png')

    def draw(self):
        self.image.draw(self.x,self.y)


class Peashooter:
    def __init__(self,x,y):
        self.x, self.y = x, 600 - y
        self.image = load_image('Peashooter_0.png')
        self.time=0.0
    def shoot(self,bullet):
        if self.time > 10:
            bullet.append(Bullet(self.x,self.y))
            self.time = 0.0
        self.time += 0.1

    def draw(self):
        self.image.draw(self.x, self.y)

class Bullet:
    def __init__(self,x,y):
        self.x,self.y = x,y
        self. image= load_image('PB0_R.png')
    def draw(self):
        self.image.draw(self.x,self.y)
    def move(self):
        self.x += 1


class Wallnut:
    def __init__(self, x, y):
        self.x, self.y = x, 600 - y
        self.image = load_image('WallNut_0.png')

    def draw(self):
        self.image.draw(self.x, self.y)