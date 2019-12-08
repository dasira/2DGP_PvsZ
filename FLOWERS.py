from pico2d import *
import game_framework
import game_world
import random


#각 객체마다 수업에서 배운 상태 추가해서 구현하는 것이 더 좋을 것 같음
#숫자 줘서 구분합시다

# Boy Run   Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Sunflower:
    def __init__(self, x, y, sun):
        self.x,self.y = x, 600-y
        self.HP = 5
        self.damageS = 0
        self.image = load_image('SunFlower_0.png')
        self.time=0.0

    def update(self):
        self.time += 0.1
        if self.time > 30:
            self.time=0.0
            s = Sun(self.x, self.y)
            return s

        pass

    def draw(self):
        self.image.draw(self.x,self.y)

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




pIDLE_CHECK, pATTACK_CHECK = range(2)

class IdleState:
    @staticmethod
    def enter(p, event):
        pass
    @staticmethod
    def exit(p, event):
        pass
    @staticmethod
    def do(p):
        pass
    @staticmethod
    def draw(p):
        pass

class AttackState:
    @staticmethod
    def enter(p, event):
        pass
    @staticmethod
    def exit(p, event):
        pass
    @staticmethod
    def do(p):
        pass
    @staticmethod
    def draw(p):
        pass

next_state_table = {
    IdleState: {pATTACK_CHECK: AttackState},
    AttackState: {pIDLE_CHECK: IdleState}
}

class Peashooter:
    def __init__(self,x,y):
        self.x, self.y = x, 600 - y
        self.image = load_image('Peashooter_0.png')
        self.damage = 1
        self.damageS = 0
        self.HP = 5
        self.shootS = 0
        self.time=0.0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    #def shoot(self,bullet):
        #if self.time > 10:
            #bullet.append(Bullet(self.x,self.y))
            #self.time = 0.0
        #self.time += 0.1
    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.image.draw(self.x, self.y)

class Bullet:
    def __init__(self,x,y):
        self.x,self.y = x,y
        self. image= load_image('PB0_R.png')
    def draw(self):
        self.image.draw(self.x,self.y)
    def move(self):
        self.x += RUN_SPEED_PPS * game_framework.frame_time


class Wallnut:
    def __init__(self, x, y):
        self.x, self.y = x, 600 - y
        self.HP = 10
        self.damageS = 0
        self.image = load_image('WallNut_0.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y)