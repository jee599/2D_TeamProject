
import random
import json
import os
from pico2d import *

import game_framework
import title_state

name = "Main State"

life = None
boy = None
font = None
speed = 20
bgm = None
score = 0
stage = 0
Box = 0
font = None

def handle_events():
    global running
    events = get_events()

class Life:
    def __init__(self):
        self.image = load_image('Resource/nomlife.png')
        self.switch = 5
    def draw(self):
        global stage
        if(stage == 0):
            for i in range(self.switch):
                self.image.clip_draw(0, stage*50, 50, 50, 300 +i * 50, 520)
        elif(stage == 1):
            for i in range(self.switch):
                self.image.clip_draw(0, stage*50, 50, 50, 80, 250 +i*50)
        elif(stage == 2):
            for i in range(self.switch):
                self.image.clip_draw(0, stage * 50, 50, 50, 450 - i * 50, 80)
        elif (stage == 3):
            for i in range(self.switch):
                self.image.clip_draw(0, stage * 50, 50, 50, 720, 350 - i * 50)
    pass

class Background:
    image = None
    image1 = None
    def __init__(self):
        if Background.image == None:
            Background.image = load_image('Resource/back1.png')
        if Background.image == None:
            Background.image = load_image('Resource/back2.png')
        self.frame = 0
        self.timer = 0
        self.limit = 10
    def update(self):
        self.timer += 1
        if self.timer > self.limit*4:
            self.timer = 0
        if self.timer < self.limit:
            self.frame = 0
        elif self.timer < self.limit*2:
            self.frame = 1
        elif self.timer < self.limit*3:
            self.frame = 2
        else:
            self.frame = 3
    def draw(self):
        self.image.clip_draw((self.frame*800), 0, 800,600, 400, 300)
class Background2:
    SCROLL_SPEED_PPS = 200
    image = None
    def __init__(self):
        if Background2.image == None:
            Background2.image = load_image('Resource/skull7.png')
        self.x = 500
        self.frame = 1
        self.left = 0
        self.speed = 3
        self.screen_width = 800
        self.screen_height = 600
        pass

    def draw(self):
        x = int(self.left)
        w = min(Background2.image.w - x, self.screen_width)
        Background2.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        Background2.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)

    def update(self):
        self.left = (self.left + self.frame * self.speed) % self.image.w

class Wall:
    def __init__(self):
        self.image = load_image('Resource/back.png')

    def draw(self):
        self.image.draw(400,300)

class Object:
    def __init__(self):
        self.image = load_image('Resource/bat1.png')
        self.frame = 0
        self.x = random.randint(600,800)
        self.speed = random.randint(7,20)
        self.y = random.randint(50,500)

    def get_box(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_box())

    def new(self):
        self.x = 800
        self.speed = random.randint(3, 15)
        self.y = random.randint(50, 500)

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x = self.x - self.speed

        if self.x <  20:
            self.x = 800
            self.speed = random.randint(3,15)
            self.y = random.randint(50,500)
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 90, 90, self.x, self.y)
class Object2:
    def __init__(self):
        self.image = load_image('Resource/bat1.png')
        self.frame = 0
        self.x = random.randint(600,800)
        self.speed = random.randint(7,17)
        self.y = random.randint(50,500)

    def get_box(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_box())

    def update(self):
        self.frame = (self.frame + 1)%6
        self.x = self.x - self.speed
        if self.x <  50:
            self.x = 800
            self.speed = random.randint(3,15)
            self.y = random.randint(50,500)
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 90, 90, self.x, self.y)

class Grass:
    SCROLL_SPEED_PPS = 200
    image = None
    def __init__(self):
        if Grass.image == None:
            Grass.image = load_image('Resource/tile2.png')
        self.x = 200
        self.frame = 1
        self.left = 0
        self.speed = 20
        self.screen_width = 800
        self.screen_height = 75
        pass

    def draw(self):
        x = int(self.left)
        w = min(Grass.image.w - x, self.screen_width)
        Grass.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        Grass.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)

    def update(self):
        self.frame = 1
        self.left = (self.left + self.frame * self.speed) % self.image.w

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_box()
    left_b, bottom_b, right_b, top_b = b.get_box()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

class Boy:
    global x
    def __init__(self):
        self.x, self.y = 100, 70
        self.frame = 0
        self.time = 0
        self.time2 = 0
        #self.image1 = load_image('Resource/animation_sheet2.png)
        self.image = load_image('Resource/animation_sheet1.png')
        self.dir = 1
        self.state = 0
        x = self.x

    def get_box(self):
        return self.x - 20, self.y - 45, self.x + 40, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_box())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state == 0:
                self.state = 1
                self.time = 0
            elif self.state == 1:
                self.state = 2
                self.time2 = 0
    def update(self):
        global stage, score
        self.frame = (self.frame + 1) % 8
        self.time = self.time + 1
        self.time2 = self.time2 + 1
        if self.y < 70:
            self.y = 70
            self.state = 0
        if self.state == 1:
            self.y = self.y + 30 - 9.8*self.time/2
            if self.y < 70:
                self.y = 70
                self.state = 0
        if self.state == 2:
            self.y = self.y + 30 - 9.8*self.time2/2
            if self.y < 70 :
                self.y = 70
                self.state = 0
    def draw(self):
        if self.state != 4:
            self.image.clip_draw((self.frame * 100), 0, 100, 100, self.x, self.y)

def enter():
    global boy, wall, back, team, back1, life, bgm, font
    boy = Boy()
    life = Life()
    wall = Wall()
    back = Background()
    #back1 = Background2()
    team = [Object() for i in range(6)]

    bgm=load_music('Nomplay.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    pass

def exit():
    global boy, wall, back, back1, life, team,bgm,font
    del(boy)
    del(bgm)
    del(font)
    del(team)
    del(life)
    del(wall)
    del(back)
    del(back1)
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    global Box
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.chage_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_TAB:
            if Box == 0:
                Box = 1
            else:
                Box = 0
        else:
            boy.handle_event(event)

    pass

def update():
    global score, font, bgm, Box

    if Box == 1:
        score += 1
    else :
        score += 2
    boy.update()
    back.update()
    #back1.update()
    for Object in team:
        Object.update()
    pass

def draw():
    global score,font,bgm,ife,Box

    clear_canvas()
    back.draw()
    #back1.draw()
    wall.draw()
    life.draw()
    boy.draw()
    if Box == 1:
        boy.draw_bb()

    if font == None:
        font = load_font('Resource\ENCR10B.TTF')
    if(Box == 1):
        font.draw(350,450 ,'Easy')
    else:
        font.draw(350,450, 'Hard')
    font.draw(350,375,'Stage : %d' % stage)
    font.draw(350,350, 'Score : %d' % score)
    for Object in team:
        if collide(boy,Object) == False:
            Object.draw()
            if(Box == 1):
                Object.draw_bb()
        else :
            if life.switch != 0:
                life.switch -= 1
            Object.new()
    update_canvas()
    delay(0.03 + Box*0.03)
    pass