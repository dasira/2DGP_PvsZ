from pico2d import *
import random


class Zombie:
    def __init__(self):
        self.x,self.y=1400,300
        self.image = load_image('Zombie_0.png')
        self.moveS = 0
    def move(self):
        self.x -= 1

    def draw(self):
        self.image.draw(self.x, self.y)
