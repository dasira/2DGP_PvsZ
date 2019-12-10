from pico2d import *
import game_framework
import random
import game_world



PIXEL_PER_METER = (10.0 / 0.3)
Helmet_PIXEL_PER_METER = (10.0 / 0.2)
Zombie_SPEED_KMPH = 2.0
Zombie_SPEED_MPM = (Zombie_SPEED_KMPH * 1000.0 / 60 )
Zombie_SPEED_MPS = (Zombie_SPEED_MPM / 60.0)
Zombie_SPEED_PPS = (Zombie_SPEED_MPS * PIXEL_PER_METER)

Helmet_Zombie_SPEED_KMPH = 6.0
Helmet_Zombie_SPEED_MPM = (Helmet_Zombie_SPEED_KMPH * 1000.0 / 60 )
Helmet_Zombie_SPEED_MPS = (Zombie_SPEED_MPM/ 60.0)
Helmet_Zombie_SPEED_PPS = (Helmet_Zombie_SPEED_MPS * Helmet_PIXEL_PER_METER)

#액션
TIME_PER_ACTION_IDLE = 2
ACTION_PER_TIME_IDLE = 1.0 / TIME_PER_ACTION_IDLE
FRAMES_PER_ACTION_IDLE = 11
#워크
TIME_PER_ACTION_WALK = 3
ACTION_PER_TIME_WALK = 1.0 / TIME_PER_ACTION_WALK
FRAMES_PER_ACTION_WALK = 17
FRAMES_PER_ACTION_WALK2 = 14
FRAMES_PER_ACTION_WALK3 = 20
#공격
TIME_PER_ACTION_ATTACK = 2
ACTION_PER_TIME_ATTACK = 1.0 / TIME_PER_ACTION_WALK
FRAMES_PER_ACTION_ATTACK = 20
# 죽음
TIME_PER_ACTION_Dead = 3.5
ACTION_PER_TIME_Dead = 1.0 / TIME_PER_ACTION_Dead
FRAMES_PER_ACTION_Dead = 9



class Zombie:
    IDLE, WALK, ATTACK ,HEAD_DOWN , DIE , Remove = 0, 1, 2 ,3 , 4 , 5
    start_frame = 0
    order = 0
    Basic_Zombies = None
    Basic_Zombies_Walk = None
    Basic_Zombies_Head = None
    Basic_Zombies_NO_Head = None
    Basic_Zombies_Die = None
    Basic_Zombies_Attack = None

    def __init__(self):
        self.x, self.y = random.randint(1950 , 2200) , random.randint(100 , 450)
        self.frame = random.randint(0, 11)
        self.Line = 2
        self.state = self.IDLE
        self.collide = False
        self.head = 0
        self.velocity = Zombie_SPEED_PPS
        self.Zombie_time = 0
        self.Attack_time =0
        if(self.Basic_Zombies == None):
            self.Basic_Zombies = load_image('Tutorial/basic_zombie_idle.png')
        if (self.Basic_Zombies_Walk == None):
            self.Basic_Zombies_Walk = load_image('Tutorial/Tutorial_Zombie_walk.png')
        if (self.Basic_Zombies_Head == None):
            self.Basic_Zombies_Head = load_image('Tutorial/Tutorial_Zombie_head.png')
        if(self.Basic_Zombies_NO_Head == None):
            self.Basic_Zombies_NO_Head = load_image('Tutorial/Tutorial_Zombie_nohead_walk.png')
        if(self.Basic_Zombies_Die == None):
            self.Basic_Zombies_Die = load_image('Tutorial/Tutorial_Zombie_nohead_Die.png')
        if(self.Basic_Zombies_Attack == None):
            self.Basic_Zombies_Attack = load_image('Tutorial/Tutorial_Zombie_Attack.png')

        self.hp = 5
        self.world_time = get_time()
    def update(self):
        self.world_time = get_time()
        self.y = (self.Line + 1) * 100

        if(self.state == self.IDLE):
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME_IDLE * game_framework.frame_time ) % 11

        if(self.state == self.WALK):
            self.frame = (self.frame + FRAMES_PER_ACTION_WALK * ACTION_PER_TIME_WALK * game_framework.frame_time) % 17
            self.x -= self.velocity * game_framework.frame_time
            self.get_bb()

            if(self.hp <= 0):
                self.state = self.HEAD_DOWN
                self.head = 1
                self.Zombie_time = get_time()
        if (self.state == self.ATTACK):
            if (self.hp <= 0):
                self.state = self.HEAD_DOWN
                self.head = 1
                self.Zombie_time = get_time()
        if(self.state == self.HEAD_DOWN):
            self.frame = (self.frame + FRAMES_PER_ACTION_WALK * ACTION_PER_TIME_WALK * game_framework.frame_time) % 17
            self.x -= self.velocity * game_framework.frame_time
            if(self.world_time - self.Zombie_time > 2):
                self.state = self.DIE
                self.Zombie_time = get_time()
                self.frame = 0
        if (self.state == self.DIE):
            if(self.frame > 8):
                if(self.world_time - self.Zombie_time > 5):
                    self.state = self.Remove
                    game_world.remove_object(self)
            elif(self.frame < 8):
                self.frame = (self.frame + FRAMES_PER_ACTION_Dead * ACTION_PER_TIME_Dead * game_framework.frame_time) % 9
        if (self.state == self.ATTACK):
            if(self.world_time - self.Attack_time > 1):
                self.Attack_time = get_time()
            self.frame = (self.frame + FRAMES_PER_ACTION_ATTACK * ACTION_PER_TIME_ATTACK * game_framework.frame_time) % 20

        for i in range(0, 5):
            if self.Line == i and self.state != self.IDLE:
                self.y = self.y = (i + 1) * 100

    def draw(self):
        if(self.state == self.IDLE):
            self.Basic_Zombies.clip_draw(int(self.frame) * 166, 0, 81, 120, self.x , self.y)
        if(self.state == self.WALK):
            self.Basic_Zombies_Walk.clip_draw(int(self.frame) * 166 - 3, 0, 90, 128, self.x, self.y)
        if (self.state == self.HEAD_DOWN):
            self.Basic_Zombies_NO_Head.clip_draw(int(self.frame) * 181 - 3, 0, 90, 95, self.x, self.y , 90 , 100)
        if (self.state == self.DIE):
            self.Basic_Zombies_Die.clip_draw(int(self.frame) * 173 - 20, 0, 180, 95, self.x, self.y)
        if (self.state == self.ATTACK):
            self.Basic_Zombies_Attack.clip_draw(int(self.frame) * 181 - 3, 0, 90, 128, self.x, self.y)

    def Attack(self):
        pass
    def get_bb(self):
        return self.x - 25, self.y - 30, self.x + 25, self.y + 30
    def draw_bb(self):
        draw_rectangle(*self.get_bb())



class Bucket_Zombie():
    IDLE, WALK, ATTACK, HEAD_DOWN, DIE, Remove = 0, 1, 2, 3, 4, 5
    Buket_IDLE = None
    Buket_Walk = None
    Buket_Attack = None
    Basic_Zombies_NO_Head = None
    Basic_Zombies_Die = None

    def __init__(self):

        if(self.Buket_IDLE == None):
            self.Buket_IDLE = load_image('Stage1/Buket_Zombie_Idle.png')
        if (self.Buket_Walk == None):
            self.Buket_Walk = load_image('Stage1/Buket_Zombie_Walk.png')
        if (self.Buket_Attack == None):
            self.Buket_Attack = load_image('Stage1/BuketAttack.png')
        if (self.Basic_Zombies_NO_Head == None):
            self.Basic_Zombies_NO_Head = load_image('Tutorial/Tutorial_Zombie_nohead_walk.png')
        if (self.Basic_Zombies_Die == None):
            self.Basic_Zombies_Die = load_image('Tutorial/Tutorial_Zombie_nohead_Die.png')

        self.x, self.y = random.randint(1950 , 2200), random.randint(100, 450)
        self.frame = random.randint(0, 11)
        self.Line = 2
        self.state = self.IDLE
        self.collide = False
        self.head = 0
        self.velocity = Zombie_SPEED_PPS
        self.Zombie_time = 0
        self.Attack_time = 0
        self.hp = 11
    def draw(self):
        if (self.state == self.IDLE):
            self.Buket_IDLE.clip_draw(int(self.frame) * 196 , 0, 176, 134, self.x, self.y)
        if (self.state == self.WALK):
            self.Buket_Walk.clip_draw(int(self.frame) * 196 - 9  ,0, 176, 142, self.x, self.y)

        if (self.state == self.ATTACK):
            self.Buket_Attack.clip_draw(int(self.frame) * 196 , 0 , 176, 142 , self.x , self.y)
        if (self.state == self.HEAD_DOWN):
            self.Basic_Zombies_NO_Head.clip_draw(int(self.frame) * 181 - 3, 0, 90, 95, self.x, self.y , 90 , 100)
        if (self.state == self.DIE):
            self.Basic_Zombies_Die.clip_draw(int(self.frame) * 173 - 20, 0, 180, 95, self.x, self.y)

    def update(self):
        self.world_time = get_time()
        self.y = (self.Line + 1) * 100
        if(self.state == self.IDLE):
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME_IDLE * game_framework.frame_time ) % 5
        if (self.state == self.WALK):
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME_IDLE * game_framework.frame_time) % 14
            self.x -= self.velocity * game_framework.frame_time
            if(self.hp <= 0):
                self.state = self.HEAD_DOWN
                self.head = 1
                self.Zombie_time = get_time()
        if (self.state == self.ATTACK):
            if (self.world_time - self.Attack_time > 1):
                self.Attack_time = get_time()
            self.frame = (self.frame + FRAMES_PER_ACTION_ATTACK * ACTION_PER_TIME_ATTACK * game_framework.frame_time) % 10
            self.get_bb()
        for i in range(0, 5):
            if self.Line == i and self.state != self.IDLE:
                self.y = self.y = (i + 1) * 100




        if (self.state == self.ATTACK):
            if (self.hp <= 0):
                self.state = self.HEAD_DOWN
                self.head = 1
                self.Zombie_time = get_time()
        if(self.state == self.HEAD_DOWN):
            self.frame = (self.frame + FRAMES_PER_ACTION_WALK * ACTION_PER_TIME_WALK * game_framework.frame_time) % 17
            self.x -= self.velocity * game_framework.frame_time
            if(self.world_time - self.Zombie_time > 2):
                self.state = self.DIE
                self.Zombie_time = get_time()
                self.frame = 0

        if (self.state == self.DIE):
            if(self.frame > 8):
                if(self.world_time - self.Zombie_time > 5):
                    self.state = self.Remove
                    game_world.remove_object(self)
            elif(self.frame < 8):
                self.frame = (self.frame + FRAMES_PER_ACTION_Dead * ACTION_PER_TIME_Dead * game_framework.frame_time) % 9

    def get_bb(self):
        return self.x - 75, self.y - 30, self.x - 25, self.y + 30
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Cone_Zombie:
    IDLE, WALK, ATTACK, HEAD_DOWN, DIE, Remove = 0, 1, 2, 3, 4, 5
    Cone_Zombie_IDLE = None
    Cone_Zombie_Walk = None
    Cone_Zombie_Attack = None
    Basic_Zombies_NO_Head = None
    Basic_Zombies_Die = None

    def __init__(self):

        if(self.Cone_Zombie_IDLE == None):
            self.Cone_Zombie_IDLE = load_image('Stage1/Cone_Zombie_Idle.png')
        if (self.Cone_Zombie_Walk == None):
            self.Cone_Zombie_Walk = load_image('Stage1/Cone_Zombie_Walk.png')
        if (self. Cone_Zombie_Attack == None ):
            self.Cone_Zombie_Attack = load_image('Stage1/Cone_Zombie_Attack.png')
        if (self.Basic_Zombies_NO_Head == None):
            self.Basic_Zombies_NO_Head = load_image('Tutorial/Tutorial_Zombie_nohead_walk.png')
        if (self.Basic_Zombies_Die == None):
            self.Basic_Zombies_Die = load_image('Tutorial/Tutorial_Zombie_nohead_Die.png')


        self.x, self.y = random.randint(1950 , 2200), random.randint(100, 450)
        self.frame = random.randint(0, 11)
        self.Line = 2
        self.state = self.IDLE
        self.collide = False
        self.head = 0
        self.velocity = Zombie_SPEED_PPS
        self.Zombie_time = 0
        self.Attack_time = 0
        self.hp = 9

    def draw(self):
        if (self.state == self.IDLE):
            self.Cone_Zombie_IDLE.clip_draw(int(self.frame) * 196, 0, 176, 143, self.x, self.y)
        if (self.state == self.WALK):
            self.Cone_Zombie_Walk.clip_draw(int(self.frame) * 191, 0, 176, 143, self.x, self.y)

        if (self.state == self.ATTACK):
            self.Cone_Zombie_Attack.clip_draw(int(self.frame) * 196, 0, 176, 142, self.x, self.y)
        if (self.state == self.HEAD_DOWN):
            self.Basic_Zombies_NO_Head.clip_draw(int(self.frame) * 181 - 3, 0, 90, 95, self.x, self.y , 90 , 100)
        if (self.state == self.DIE):
            self.Basic_Zombies_Die.clip_draw(int(self.frame) * 173 - 20, 0, 180, 95, self.x, self.y)

    def update(self):
        self.world_time = get_time()
        self.y = (self.Line + 1) * 100
        if(self.state == self.IDLE):
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME_IDLE * game_framework.frame_time ) % 7
        if (self.state == self.WALK):
            self.frame = (self.frame + FRAMES_PER_ACTION_WALK3 * ACTION_PER_TIME_WALK * game_framework.frame_time) % 20
            if(self.hp <= 0):
                self.state = self.HEAD_DOWN
                self.head = 1
                self.Zombie_time = get_time()
            self.x -= self.velocity * game_framework.frame_time
        if (self.state == self.ATTACK):
            if (self.world_time - self.Attack_time > 1):
                self.Attack_time = get_time()
            self.frame = (self.frame + FRAMES_PER_ACTION_ATTACK * ACTION_PER_TIME_ATTACK * game_framework.frame_time) % 10


        if (self.state == self.ATTACK):
            if (self.hp <= 0):
                self.state = self.HEAD_DOWN
                self.head = 1
                self.Zombie_time = get_time()

        if(self.state == self.HEAD_DOWN):
            self.frame = (self.frame + FRAMES_PER_ACTION_WALK * ACTION_PER_TIME_WALK * game_framework.frame_time) % 17
            self.x -= self.velocity * game_framework.frame_time
            if(self.world_time - self.Zombie_time > 2):
                self.state = self.DIE
                self.Zombie_time = get_time()
                self.frame = 0

        if (self.state == self.DIE):
            if(self.frame > 8):
                if(self.world_time - self.Zombie_time > 5):
                    self.state = self.Remove
                    game_world.remove_object(self)
            elif(self.frame < 8):
                self.frame = (self.frame + FRAMES_PER_ACTION_Dead * ACTION_PER_TIME_Dead * game_framework.frame_time) % 9

        for i in range(0, 5):
            if self.Line == i and self.state != self.IDLE:
                self.y = self.y = (i + 1) * 100
    def get_bb(self):
        return self.x - 75, self.y - 30, self.x - 25, self.y + 30
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Helmet_Zombie:
    IDLE, WALK, ATTACK, HEAD_DOWN, DIE, Remove = 0, 1, 2, 3, 4, 5
    Helmet_Zombie_Zombie_IDLE = None
    Helmet_Zombie_Zombie_Walk = None
    Helmet_Zombie_Zombie_Attack = None
    Helmet_Zombie_Die = None

    def __init__(self):
        if(self.Helmet_Zombie_Zombie_IDLE == None):
            self.Helmet_Zombie_Zombie_IDLE = load_image('Stageleveltwo/helmetZombie_Idle.png')
        if (self.Helmet_Zombie_Zombie_Walk == None):
            self.Helmet_Zombie_Zombie_Walk = load_image('Stageleveltwo/Helmet_Zombie_walk.png')
        if (self. Helmet_Zombie_Zombie_Attack == None ):
            self.Helmet_Zombie_Zombie_Attack = load_image('Stageleveltwo/Helmet_Zombie_Attack.png')
        if (self.Helmet_Zombie_Die == None):
            self.Helmet_Zombie_Die = load_image('Stageleveltwo/Helmet_Zombie_die.png')

        self.Basic_Zombies_Die = load_image('Tutorial/Tutorial_Zombie_nohead_Die.png')
        self.x, self.y = random.randint(1700, 1800), random.randint(100, 450)
        self.frame = random.randint(0, 11)
        self.Line = 2
        self.state = self.IDLE
        self.collide = False
        self.head = 0
        self.velocity = Helmet_Zombie_SPEED_PPS
        self.Zombie_time = 0
        self.Attack_time = 0
        self.hp = 13
    def draw(self):
        if (self.state == self.IDLE):
            self.Helmet_Zombie_Zombie_IDLE.clip_draw(int(self.frame) * 184, 0, 176, 143, self.x, self.y)
        if (self.state == self.WALK):
            self.Helmet_Zombie_Zombie_Walk.clip_draw(int(self.frame) * 184 - 10, 0, 176, 160, self.x, self.y)

        if (self.state == self.ATTACK):
            self.Helmet_Zombie_Zombie_Attack.clip_draw(int(self.frame) * 184, 0, 176, 142, self.x, self.y)
        if (self.state == self.DIE):
            self.Helmet_Zombie_Die.clip_draw(int(self.frame) * 274, 0, 180, 130, self.x, self.y)
    def update(self):
        self.world_time = get_time()
        self.y = (self.Line + 1) * 100

        if(self.state == self.IDLE):
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME_IDLE * game_framework.frame_time ) % 14
        if (self.state == self.WALK):
            self.frame = (self.frame + FRAMES_PER_ACTION_WALK3 * ACTION_PER_TIME_WALK * game_framework.frame_time) % 10
            if(self.hp <= 0):
                self.state = self.DIE #
                self.Zombie_time = get_time()
                self.frame = 0

            self.x -= self.velocity * game_framework.frame_time
        if (self.state == self.ATTACK):
            if (self.world_time - self.Attack_time > 1):
                self.Attack_time = get_time()
            self.frame = (self.frame + FRAMES_PER_ACTION_ATTACK * ACTION_PER_TIME_ATTACK * game_framework.frame_time) % 9

        if (self.state == self.DIE):
            if(self.frame >= 5):
                if(self.world_time - self.Zombie_time > 5):

                    self.state = self.Remove
                    game_world.remove_object(self)
            elif(self.frame < 5):
                self.frame = (self.frame + FRAMES_PER_ACTION_Dead * ACTION_PER_TIME_Dead * game_framework.frame_time) % 6



        if (self.state == self.ATTACK):
            if (self.hp <= 0):
                self.state = self.DIE
                self.frame = 0
                self.Zombie_time = get_time()

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())