from pico2d import *

import game_framework
import game_world
import random


from zombies import Zombie
from zombies import Bucket_Zombie
from zombies import Cone_Zombie
from plants import Peashooter
from plants import Sunflower
from plants import Walnut
from plants import SunLight
from bullets import Bullet




PIXEL_PER_METER = (10.0 / 0.3)
#이동거리가 10pixsel 에 30cm간다는 뜻 임의로 정함
CHANGE_SPEED_KMPH = 10.0
# 10.0 속도
#  10.0 속도 =  km / hour 킬로미터 거리 / 시간
CHANGE_SPEED_MPM = (CHANGE_SPEED_KMPH * 1000.0 / 60 )
# 경과시간을 분으로 바꿈 (속도 * 1000 / 60)
CHANGE_SPEED_MPS = (CHANGE_SPEED_MPM / 60.0)
# 경과시간을 초로 바꿈
CHANGE_SPEED_PPS = (CHANGE_SPEED_MPS * PIXEL_PER_METER) # 픽셀 퍼 세크 미터 퍼세크에다가 픽셀퍼 미터를 곱한것
#거리 = 시간 * 속도


Peashooters = []
Sunflowers = []
Walnuts = []
Zombies = []

ALLPLANT=[Peashooters, Sunflowers]

Sun = []
Bullets = []
Zombie_Count = 0
Plant_Count = 0
Sun_Count = 0
Bullet_Count = 0


PRE01, PRE02, PRE03, MAIN  = range(4)

next_state_table = {
(SDL_KEYDOWN, SDLK_1): PRE02,
(SDL_KEYDOWN,SDLK_2) : MAIN
}



def shine():
    global Sun, Sun_Count
    new_Sun = SunLight()
    Sun.append(new_Sun)
    game_world.add_object(new_Sun, 1)
    Sun_Count += 1


def Fshine(x_, y_):
    global Sun, Sun_Count
    new_Sun = SunLight()
    new_Sun.x = x_
    new_Sun.y = y_ + 20
    new_Sun.limit_y = y_ - 10
    Sun.append(new_Sun)
    game_world.add_object(new_Sun, 1)
    Sun_Count += 1
    pass


def shoot( x , y ):
    global Bullets , Bullet_Count
    New_Bullet = Bullet(x + 30, y )
    Bullets.append(New_Bullet)
    game_world.add_object(New_Bullet, 1)
    Bullet_Count += 1

def makeZombie():
    global Zombies , Zombie_Count
    new_zombie = Zombie()
    new_zombie.Line = random.randint(0 , 4)
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count +1

def makeBZombie():
    global Zombies, Zombie_Count
    new_zombie = Bucket_Zombie()
    new_zombie.Line = random.randint(0, 4)
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count + 1

def makeCZombie():
    global Zombies, Zombie_Count
    new_zombie = Cone_Zombie()
    new_zombie.Line = random.randint(0, 4)
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count + 1

def plant_Plants( x, y , Line_, select ,sitting):
    global Peashooters , Plant_Count
    if(select == 1):
        new_plant = Peashooter(x, y, Line_, sitting)
        game_world.add_object(new_plant, 1)
        Peashooters.append(new_plant)
        Plant_Count = Plant_Count + 1
    elif(select == 2):
        new_plant = Sunflower(x, y, Line_, sitting)
        game_world.add_object(new_plant, 1)
        Sunflowers.append(new_plant)
        Plant_Count = Plant_Count + 1
    elif (select == 3):
        new_plant = Walnut(x, y, Line_, sitting)
        game_world.add_object(new_plant, 1)
        Walnuts.append(new_plant)
        Plant_Count = Plant_Count + 1



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False
    return True


def Collide_check(stage01):
    global Zombies , Peashooters , Bullets
    global Plant_Count

    for Zombie in Zombies:
        for Bullet in Bullets:
            if collide(Bullet, Zombie) and Bullet.state == 0 and Zombie.hp > 0 and Zombie.state != 3 and Zombie.state != 4 and  Zombie.state !=5:
                Zombie.hp -=  1
                Bullet.state = 1
                break

    for plant in Peashooters:
        for Zombie in Zombies:
            if collide(plant, Zombie) and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5:
                Zombie.state = 2
                Zombie.collide = True
                plant.state = 3

            elif (Zombie.collide != True  and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5):
                Zombie.state = 1
            else:
                plant.state = 0


    for Flower in Sunflowers:
        for Zombie in Zombies:
            if collide(Flower, Zombie) and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5:
                Zombie.state = 2
                Zombie.collide = True
                Flower.state = 3

            elif (Zombie.collide != True and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5):
                Zombie.state = 1

            elif (Zombie.collide != True and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5):
                Zombie.state = 1

            else:
                Flower.state = 1
    for walnut in Walnuts:
        for Zombie in Zombies:
            if collide(walnut, Zombie) and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5:
                Zombie.state = 2
                Zombie.collide = True
                walnut.state = 3

            elif (Zombie.collide != True and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5):
                Zombie.state = 1
            else:
                walnut.state = 0

    for Zombie in Zombies:
        Zombie.collide = False
        if(Plant_Count == 0  and Zombie.state != 3 and Zombie.state != 4 and  Zombie.state != 5):
            Zombie.state = 1

    for Bullet in Bullets:
        if(Bullet.action > 20 and Bullet.state == 1):
            Bullet.state = 2
    pass


def Delete_all():
    global Zombies, Peashooters, Bullets
    global Zombie_Count
    global Plant_Count
    for Zombie in Zombies:
        if(Zombie.state == 5):
            Zombies.remove(Zombie)
            del Zombie
            Zombie_Count = Zombie_Count - 1

    for Bullet in Bullets:
        if(Bullet.state == 2):
            Bullets.remove(Bullet)
            del Bullet



def clear():
    global Zombies, Peashooters, Bullets , Sun , Sunflowers, Walnuts
    global Zombie_Count
    global Plant_Count
    global Bullet_Count
    del Zombies
    del Peashooters
    del Bullets
    del Sun
    del Sunflowers
    del Walnuts

    Zombies = []
    Peashooters = []
    Sun = []

    Bullets = []
    Sunflowers = []
    Walnuts = []
    Plant_Count =0
    Zombie_Count =0
    Bullet_Count=0



class Start_state:
    @staticmethod
    def enter(stage01 ,event):
        stage01.start_time = get_time()

    @staticmethod
    def exit(stage01 , event):
        pass

    @staticmethod
    def do(stage01):
        if (stage01.timer - stage01.start_time >= 2):
            stage01.add_event(PRE02)

    @staticmethod
    def draw(stage01):
        stage01.stage01_image.clip_draw(int(stage01.moveX), 0, 800, 600, 700, 300, 1400, 600)
        stage01.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        stage01.cards.clip_draw(0, 488, 62, 87, 140, 560, 63, 67)
        stage01.cards.clip_draw(65, 488, 62, 87, 210, 560, 63, 67)
        stage01.cards.clip_draw(195, 488, 62, 87, 137 + 124 + 22, 560, 63, 67)
        stage01.shovel.draw(600, 560)

        stage01.font.draw(28, 532, '%d' % stage01.money)

        #self.card.clip_draw(0, 488, 62, 87, 138, 600 - (109 // 2) - 1)
        #self.card.clip_draw(65, 488, 62, 87, 137 + 62 + 11, 600 - (109 // 2) - 1)
        #self.card.clip_draw(195, 488, 62, 87, 137 + 124 + 22, 600 - (109 // 2) - 1)
        stage01.font.draw(500, 300, '길 건너편에 좀비가 보인다...', (255,255,255))




class Move_state:
    global Zombies , Zombie_Count
    @staticmethod
    def enter(stage01 , event):
        stage01.velocity += CHANGE_SPEED_PPS
        stage01.moveX = 0
        stage01.move = 0
        stage01.start_time = 0

        for i in range(2):
            makeZombie()
            makeBZombie()
            makeCZombie()

    @staticmethod
    def exit(stage01,event):
        global Zombies, Zombie_Count
        for Zombie in Zombies:
            Zombies.remove(Zombie)
            del Zombie
            Zombie_Count = Zombie_Count - 1

    @staticmethod
    def do(stage01):
        if (stage01.move == 0):
            stage01.moveX += stage01.velocity * game_framework.frame_time
            for Zombie in Zombies:
                Zombie.x -= (stage01.velocity * game_framework.frame_time) * 1.71
            if (stage01.moveX > 500):
                stage01.start_time = get_time()
                stage01.move = 1

        elif(stage01.move == 1):
            if (stage01.timer - stage01.start_time >= 3):
                stage01.start_time = get_time()
                stage01.move = 2

        elif (stage01.move == 2):
            stage01.moveX -= stage01.velocity * game_framework.frame_time
            for Zombie in Zombies:
                Zombie.x += (stage01.velocity * game_framework.frame_time) * 1.71
            if (stage01.moveX <= 250):
                stage01.move = 3
                stage01.start_time = get_time()

        elif (stage01.move == 3):
            if (stage01.timer - stage01.start_time >= 3):
                stage01.add_event(MAIN)

    @staticmethod
    def draw(stage01):
        stage01.stage01_image.clip_draw(int(stage01.moveX), 0, 800, 600, 700, 300, 1400, 600)
        stage01.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        stage01.cards.clip_draw(0, 488, 62, 87, 140, 560, 63, 67)
        stage01.cards.clip_draw(65, 488, 62, 87, 210, 560, 63, 67)
        stage01.cards.clip_draw(195, 488, 62, 87, 137 + 124 + 22, 560, 63, 67)
        stage01.shovel.draw(600, 560)

        stage01.font.draw(28, 532, '%d' % stage01.money)
        stage01.font.draw(500, 300, '좀비들이 길을 건너올 것 같다.', (255, 255, 255))




class Stage_state:
    global Peashooters , Plant_Count

    @staticmethod
    def enter(stage01 , event):
        stage01.moveX = 250
        stage01.frame = 0
        stage01.stage_time = get_time()
        stage01.time_bar_time = get_time()

        stage01.game_over_time = 0

        for i in range(5):
            makeZombie()
            makeBZombie()
            makeCZombie()

        for Zombie in Zombies:
            Zombie.state = 1
            Zombie.x = 1700
            Zombie.frame = random.randint(0 , 17)

        for i in range(Zombie_Count):
            Zombies[i].x += i * (random.randint(100, 150) + 50)


    @staticmethod
    def exit(stage01 , event):
        pass

    @staticmethod
    def do(stage01):
        global Plant_Count

        if (stage01.timer - stage01.time_bar_time >= 1):
            if (stage01.timebar <= 300):
                stage01.timebar = (21 - Zombie_Count) * 14

                stage01.time_bar_time = get_time()

        if (stage01.timer - stage01.stage_time > 5):
            stage01.stage_time = get_time()
            shine()

        for plant in Peashooters:
            for i in range(Zombie_Count):
                if ((plant.Line == Zombies[i].Line) and Zombies[i].x < 1400 and Zombies[i].state != 4):
                    plant.state = 2
                    plant.checkline =True

                if(((plant.Line != Zombies[i].Line) or Zombies[i].x > 1400) and plant.checkline != True):
                    plant.state = 1
                    plant.checkline = False

            if(Zombie_Count == 0):
                plant.state = 1

        for plant in Peashooters:
            if(plant.state == 2):
                if (stage01.timer - plant.state_time > 3):
                    shoot(plant.x , plant.y + 30)
                    plant.state_time = get_time()
        for Flower in Sunflowers:
            if(Flower.state == 1):
                if stage01.timer - Flower.Sun_time > 20:
                    Fshine(Flower.x , Flower.y)
                    Flower.Sun_time = get_time()

        Collide_check(stage01)

        for plant in Peashooters:
            if (plant.state == 3 and plant.hp <= 0):
                for i in range(len(stage01.count)):
                    if (plant.sitting == stage01.count[i]):
                        stage01.count.remove(plant.sitting)
                        game_world.remove_object(plant)
                        Peashooters.remove(plant)
                        Plant_Count = Plant_Count - 1
                        break
                break

        for Flower in Sunflowers:
            if (Flower.state == 3 and Flower.hp <= 0):
                for i in range(len(stage01.count)):
                    if (Flower.sitting == stage01.count[i]):
                        stage01.count.remove(Flower.sitting)
                        game_world.remove_object(Flower)
                        Sunflowers.remove(Flower)
                        Plant_Count = Plant_Count - 1
                        break
                break

        for walnut in Walnuts:
            if (walnut.state == 3 and walnut.hp <= 0):
                for i in range(len(stage01.count)):
                    if (walnut.sitting == stage01.count[i]):
                        stage01.count.remove(walnut.sitting)
                        game_world.remove_object(walnut)
                        Walnuts.remove(walnut)

                        Plant_Count = Plant_Count - 1
                        break

                break

        Delete_all()

        if (stage01.game_over == 0):
            for Zombie in Zombies:
                if (Zombie.x < 0):
                    stage01.game_over = 1
        if (stage01.game_over == 1):
            stage01.game_over_time = get_time()
            stage01.game_over = 2

        if(Zombie_Count == 0 and stage01.win == 0):
            stage01.win = 1






    @staticmethod
    def draw(stage01):
        stage01.stage01_image.clip_draw(int(stage01.moveX), 0, 800, 600, 700, 300, 1400, 600)
        stage01.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        stage01.cards.clip_draw(0, 488, 62, 87, 140, 560, 63, 67)
        stage01.cards.clip_draw(65, 488, 62, 87, 210, 560, 63, 67)
        stage01.cards.clip_draw(195, 488, 62, 87, 137 + 124 + 22, 560, 63, 67)
        stage01.shovel.draw(600,560)


        if (stage01.select_card == 1):
            stage01.chooseP.clip_draw(0, 0, 84, 80, stage01.mouse_x + 10, 600 - stage01.mouse_y)
        elif (stage01.select_card == 2):
            stage01.chooseF.clip_draw(0, 0, 84, 80, stage01.mouse_x + 10, 600 - stage01.mouse_y)
        elif (stage01.select_card == 3):
            stage01.chooseW.clip_draw(0, 0, 84, 80, stage01.mouse_x + 10, 600 - stage01.mouse_y)
        elif (stage01.select_card == 10):
            stage01.chooseS.clip_draw(0, 0, 72, 76, stage01.mouse_x + 10, 600 - stage01.mouse_y)

        stage01.font.draw(28, 532, '%d' % stage01.money)
        stage01.timebar_image.clip_draw(0, 0, 300, 60, 1230, 30)
        stage01.timebar_image.clip_draw_to_origin(0, 60, 300 - stage01.timebar, 60, 1080,1)

        if (stage01.game_over > 0):
            stage01.font.draw(600, 350, '패배...', (255, 255, 255))
        if(stage01.win > 0):
            stage01.font.draw(600, 350, '승리했다!!', (255, 255, 255))


next_state_table = {
    Start_state : {PRE01 : Start_state , PRE02:Move_state , MAIN : Stage_state},
    Move_state : {PRE02: Move_state , MAIN : Stage_state},
    Stage_state : {MAIN : Stage_state}
}


class stage01:
    stage01_image = None
    board = None
    cards = None
    timebar_image = None

    def __init__(self):
        if (self.stage01_image == None ):
            self.stage01_image = load_image('Stage1/Tutorial_map.png')
        if (self.board == None):
             self.board = load_image('Stage1/board.png')

        if (self.cards == None ):
            self.cards = load_image('Stage1/cards.png')
        if (self.timebar_image == None):
            self.timebar_image = load_image('Stage1/progress_bar.png')

        self.chooseP = load_image('Tutorial/Baisc_plants.png')
        self.chooseF = load_image('Stage1/Flower.png')
        self.chooseW = load_image('Stageleveltwo/Potato_state_good.png')
        self.chooseS = load_image('Tutorial/lampa.png')

        self.shovel = load_image('Tutorial/lampa.png')
        self.font = load_font('Stage1/ConsolaMalgun.ttf', 25)

        self.win = 0
        self.timebar = 0
        self.velocity = 0

        self.moveX = 0
        self.event_que = []
        self.frame = 0
        self.cur_state = Start_state
        self.cur_state.enter(self, None)

        self.money = 300
        self.select_card = 0
        self.timer = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.game_over =0
        self.plant_setting = 0
        self.count = []

    def add_event(self , event):
        self.event_que.insert(0,event)
    def update(self):
        self.timer = get_time()
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self)
        pass

    def handle_event(self,event):
        if (self.cur_state == Stage_state and event.type == SDL_MOUSEMOTION):
            self.mouse_x = event.x
            self.mouse_y = event.y

        if (event.type == SDL_KEYDOWN):
            if (event.key == SDLK_1):
                self.add_event(MAIN)
            if (event.key == SDLK_2):
                global Zombies, Zombie_Count
                Zombies[0].x = 50
            if (event.key == SDLK_3):
                Zombie_Count = 0

        if(self.cur_state == Stage_state and event.type == SDL_MOUSEBUTTONDOWN):
            if (event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1400 and event.y >= 0 and event.y <= 600):
                global Sun_Count , Sun
                for sun in Sun:
                    if (event.x > sun.x - 50 and event.x < sun.x + 50 and 600 - event.y - 1 > sun.y - 50 and 600 - event.y - 1 < sun.y + 50):
                        sun.click = 1
                        sun.plus_x = sun.x
                        sun.plus_y = sun.y
                        Sun.remove(sun)
                        del sun

                        Sun_Count -= 1
                        self.money += 25
                        break

            if (event.button == SDL_BUTTON_RIGHT):
                self.select_card = 0  #
            if (event.button == SDL_BUTTON_LEFT and event.x > 600 - 50 and event.x < 600 + 50 and 0 + 600 - event.y - 1 < 0 + 600 and 0 + 600 - event.y - 1 > 0 + 600 - 80 and self.select_card == 0):
                  self.select_card = 10
            elif (event.button == SDL_BUTTON_LEFT and event.x > 100 and event.x < 180 and 0 + 600 - event.y - 1 < 0 + 600 and 0 + 600 - event.y - 1 > 0 + 600 - 80 and self.money >= 100 and self.select_card == 0):
                self.select_card = 1
            elif (event.button == SDL_BUTTON_LEFT and event.x > 180 and event.x < 260 and 0 + 600 - event.y - 1 < 0 + 600 and 0 + 600 - event.y - 1 > 0 + 600 - 80 and self.money >= 50 and self.select_card == 0):
                self.select_card = 2
            elif (event.button == SDL_BUTTON_LEFT and event.x > 260 and event.x < 340 and 0 + 600 - event.y - 1 < 0 + 600 and 0 + 600 - event.y - 1 > 0 + 600 - 80 and self.money >= 50 and self.select_card == 0):
                self.select_card = 3
            elif (event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1300 and 0 +600 - event.y - 1 < 600 and 0 +600 - event.y > 0 and self.select_card > 0):
                count = False
                for i in range(-1 , 4):
                    if(count == True):
                        break
                    for j in range(9):
                        self.plant_setting += 1
                        if (event.x >= j * 140 and event.x <= j * 140 + 140 and 600 - event.y -1 > (i) * 100 + 30  and 600 - event.y -1 <= (i + 1) * 100 + 130 ):
                            global Plant_Count
                            for k in range(len(self.count)):
                                if(self.plant_setting == self.count[k]):
                                    if (self.select_card == 10):
                                        for plant in Peashooters:
                                            if (plant.sitting == self.count[k]):
                                                self.count.remove(plant.sitting)
                                                Peashooters.remove(plant)
                                                Plant_Count -= 1
                                                game_world.remove_object(plant)
                                                self.select_card = 0

                                                break
                                        for Flower in Sunflowers:
                                            if (Flower.sitting == self.count[k]):
                                                self.count.remove(Flower.sitting)
                                                Sunflowers.remove(Flower)
                                                Plant_Count -= 1
                                                game_world.remove_object(Flower)
                                                self.select_card = 0

                                                break
                                        for walnut in Walnuts:
                                            if (walnut.sitting == self.count[k]):
                                                self.count.remove(walnut.sitting)
                                                Walnuts.remove(walnut)
                                                Plant_Count -= 1
                                                game_world.remove_object(walnut)
                                                self.select_card = 0

                                                break
                                    count = True
                                    self.plant_setting = 0
                                    break

                            if(count == False and self.select_card != 10):
                                if(self.select_card == 1):
                                    self.money = self.money - 100
                                elif (self.select_card == 2):
                                    self.money = self.money - 50
                                elif (self.select_card == 3):
                                    self.money = self.money - 50
                                plant_Plants(int(j * 140 + 70), i + 1, i + 1, self.select_card , self.plant_setting)
                                self.select_card = 0
                                self.count.append(self.plant_setting)
                                self.plant_setting = 0
                                count = True
                                break
                self.plant_setting = 0





