from pico2d import *
import random


#각 객체마다 수업에서 배운 상태 추가해서 구현하는 것이 더 좋을 것 같음
#숫자 줘서 구분합시다

class Sunflower:
    def __init__(self,x,y):
        self.x,self.y = x, 600-y
        self.HP = 5
        self.damageS = 0
        self.image = load_image('SunFlower_0.png')
        self.time=0.0

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x,self.y)

    def makeSun(self,sun):
        if self.time > 30:
            sun.append(Sun(self.x, self.y))
            self.time=0.0
        self.time+=0.1
        pass


class Sun:
    def __init__(self,x,y):
        if x==0 and y==0:
            self.x, self.y = 120 + (random.randint(0,8)*140) , 75 + (random.randint(0,4)*100)
        else:
            self.x, self.y = x, y
        if x == 0 and y == 0:
            self.high = 505
        else:
            self.high = y + 30
        self.image = load_image('Sun_0.png')

    def update(self):
        if self.high >= self.y:
            self.high -= 10

    def draw(self):
        self.image.draw(self.x,self.high)


class Peashooter:
    def __init__(self,x,y):
        self.x, self.y = x, 600 - y
        self.image = load_image('Peashooter_0.png')
        self.damage = 1
        self.damageS = 0
        self.HP = 5
        self.shootS = 0
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
        self.HP = 10
        self.damageS = 0
        self.image = load_image('WallNut_0.png')

    def draw(self):
        self.image.draw(self.x, self.y)