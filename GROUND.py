from pico2d import *

class Ground:
    def __init__(self):
        self.image = load_image('Tutorial_map.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(225 , 0, 800, 600, 700, 300, 1400, 600)

class UI:
    def __init__(self):
        self.image = load_image('board.png')
        self.card = load_image('cards.png')
    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0,0,557,109,(557//2),600-(109//2))
        self.card.clip_draw(0, 488,62,87, 138,600-(109//2)-1)
        self.card.clip_draw(65, 488, 62, 87, 137 + 62 + 11, 600 - (109 // 2) - 1)
        self.card.clip_draw(195, 488, 62, 87, 137 + 124 + 22, 600 - (109 // 2)-1)
        #self.card.clip
        ##66 87

