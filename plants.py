from pico2d import *
import game_framework
import game_world
import random
import time
from bullets import Bullet



# Boy Run   Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
#이동거리가 10pixsel 에 30cm간다는 뜻 임의로 정함
CHANGE_SPEED_KMPH = 5.0
# 10.0 속도
#  10.0 속도 =  km / hour 킬로미터 거리 / 시간
CHANGE_SPEED_MPM = (CHANGE_SPEED_KMPH * 1000.0 / 60 )
# 경과시간을 분으로 바꿈 (속도 * 1000 / 60)
CHANGE_SPEED_MPS = (CHANGE_SPEED_MPM / 60.0)
# 경과시간을 초로 바꿈
CHANGE_SPEED_PPS = (CHANGE_SPEED_MPS * PIXEL_PER_METER) # 픽셀 퍼 세크 미터 퍼세크에다가 픽셀퍼 미터를 곱한것

TIME_PER_ACTION = 1.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION #1초에 할 액션수 2개
FRAMES_PER_ACTION = 21 # 8개의 프레임

pTIME_PER_ACTION = 1.2
pACTION_PER_TIME = 1.0 / pTIME_PER_ACTION
pFRAMES_PER_ACTION_IDLE = 11
pFRAMES_PER_ACTION_WALK = 17


class SunLight:
    image = None
    def __init__(self):
        self.x, self.y = 120 + random.randint(0,8)*140 , 700

        self.limit_y = random.randint(50, 400)
        self.frame = random.randint(0,21)
        self.velocity = CHANGE_SPEED_PPS
        self.plus_time = 0
        self.state = 0
        self.click = 0
        self.plus_y = 0
        self.plus_x = 0

        if(SunLight.image == None):
            SunLight.image = load_image('Tutorial/Sun.png')
    def update(self):
        if self.click == 0:
            self.frame = (self.frame + FRAMES_PER_ACTION * pACTION_PER_TIME * game_framework.frame_time) % 20

        if self.limit_y <= self.y and self.click == 0:
            self.y -=  self.velocity * game_framework.frame_time

        if (self.click == 1):
            t = self.plus_time / 100
            self.x = (1 - t) * self.plus_x + t * 50
            self.y = (1 - t) * self.plus_y + t * 550

            self.plus_time += 1
            if (self.plus_time == 100):
                self.click = 2
        if (self.click == 2):
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 93, 0, 78, 79, self.x, int(self.y))




# DIE , HIT, ACT, IDLE  = 4, 3, 2, 1
class Sunflower:
    SF_image = None
    def __init__(self, x, y, l, s):
        if (self.SF_image == None):
            self.SF_image = load_image('Stage1/Flower.png')
        self.x = x
        self.y = (l + 1) * 100 - 10  # 식물 라인 설정
        self.hp = 3
        self.frame = random.randint(0, 11)

        self.state = 1
        self.Line = l  # 맨위에부터 0 1 2 3 4  개의 라인
        self.Sun_time = get_time()
        self.state_time = 0
        self.world_time =0
        self.sitting = s  # 자리

    def update(self):
        self.frame = (self.frame + pFRAMES_PER_ACTION_IDLE * pACTION_PER_TIME * game_framework.frame_time) % 17
        if (self.state == 3):  # 식물이 지금 맞고 있다.
            self.world_time = get_time()
            if (self.world_time - self.state_time > 2):
                self.state_time = get_time()
                self.hp -= 1  # 식물의 피 달음

    def draw(self): # 식물을 그려준다
        self.SF_image.clip_draw(int(self.frame) * 103 - 2, 0, 70, 90, self.x, self.y, )
    def get_bb(self):
        return self.x - 42, self.y - 15, self.x + 42, self.y + 15
    def draw_bb(self):
        draw_rectangle(*self.get_bb())


# DIE , HIT, ACT, IDLE  = 4, 3, 2, 1
class Peashooter:
    PS_image = None
    def __init__(self, x, y, l, s):
        if (self.PS_image == None):
            self.PS_image = load_image('Tutorial/Baisc_plants.png')
        self.x , self.y = x, y
        self.y = (l + 1) * 100 - 10
        self.hp = 3
        self.frame = random.randint(0, 11)

        self.checkline = False
        self.Bullet_Count = 0
        self.state = 1
        self.Line = l  # 맨위에부터 0 1 2 3 4  개의 라인
        self.state_time = 0
        self.world_time =0
        self.sitting = s  # 자리

    def update(self):
        self.frame = (self.frame + pFRAMES_PER_ACTION_IDLE * pACTION_PER_TIME * game_framework.frame_time) % 12
        if(self.state == 3): #식물이 지금 맞고 있다.
            self.world_time = get_time()
            if(self.world_time - self.state_time  > 2):
                self.state_time = get_time()
                self.hp -= 1 #식물의 피 달음
                if (self.hp <= 0):
                    self.state = 4
        if(self.state == 4):
            game_world.remove_object(self)

    def draw(self): # 식물을 그려준다
        self.PS_image.clip_draw(int(self.frame) * 86 - 2, 0, 70, 90, self.x, self.y, )
    def get_bb(self):
        return self.x - 42, self.y - 15, self.x + 42, self.y + 15
    def draw_bb(self):
        draw_rectangle(*self.get_bb())



# DIE , HIT, ACT, IDLE  = 4, 3, 2, 1
class Walnut:
    W_image = None
    def __init__(self, x, y, l, s):
        if (self.W_image == None):
            self.W_image = load_image('Stageleveltwo/Potato_state_good.png')
        self.x = x
        self.y = (l + 1) * 100 - 10  # 식물 라인 설정
        self.hp = 5
        self.frame = random.randint(0, 11)

        self.state = 1
        self.Line = l
        self.state_time = 0
        self.world_time = 0
        self.sitting = s

    def update(self):
        self.frame = (self.frame + pFRAMES_PER_ACTION_IDLE * pACTION_PER_TIME * game_framework.frame_time) % 14
        if (self.state == 3):
            self.world_time = get_time()
            if (self.world_time - self.state_time > 2):
                self.state_time = get_time()
                self.hp -= 1

    def draw(self):
        self.W_image.clip_draw(int(self.frame) * 95 - 2, 0, 70, 90, self.x, self.y, )
    def get_bb(self):
        return self.x - 42, self.y - 15, self.x + 42, self.y + 15
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

