from pico2d import *
import random


class Zombie:
    def __init__(self):
        self.x,self.y = 1400, 300
        self.image = load_image('Zombie_0.png')
        self.HP = 10
        self.Atime = 0
        self.damage = 1
        self.speed = 1
        self.moveS = 0

    def update(self):
        self.x -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

class CheadZombie:
    def __init__(self):
        self.x,self.y = 1400, 300
        self.image = load_image('ConeheadZombie_0.png')
        self.HP = 15
        self.Atime = 0
        self.damage = 2
        self.speed = 1
        self.moveS = 0

    def move(self):
        self.x -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

class BheadZombie:
    def __init__(self):
        self.x,self.y = 1400, 300
        self.image = load_image('BucketheadZombie_0.png')
        self.HP = 20
        self.Atime = 0
        self.damage = 2
        self.speed = 2
        self.moveS = 0

    def move(self):
        self.x -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)
