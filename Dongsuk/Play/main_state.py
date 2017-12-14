
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
run = 0
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
            Background.image = load_image('Resource/back0.png')
        if Background.image == None:
            Background.image1 = load_image('Resource/back2.png')
        self.frame = 0
    def update(self):
        self.frame = (self.frame + 1)%8
    def draw(self):
        self.image.clip_draw((self.frame*800), 0, 800,600, 400, 300)

class Wall:
    def __init__(self):
        self.image = load_image('Resource/back.png')

    def draw(self):
        self.image.draw(400,300)

class Object:
    def __init__(self):
        self.image = load_image('Resource/bat1.png')
        self.frame = 0
        self.x = random.randint(600,1200)
        self.speed = random.randint(7,15)
        self.y = random.randint(100,200)

    def get_box(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_box())

    def new(self):
        self.x += random.randint(500, 1000)
        self.speed = random.randint(7, 15)
        self.y = random.randint(100, 200)

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x = self.x - self.speed
        if self.frame < 4:
            self.y -= 3
        else:
            self.y += 3
        if self.x <  20:
            self.x = 800
            self.speed = random.randint(3,15)
            self.y = random.randint(50,500)
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 90, 90, self.x, self.y)
class Object2:
    def __init__(self):
        self.image = load_image('Resource/horn1.png')
        self.x = 600 + random.randint(100,1000)
        self.y = 70

    def get_box(self):
        return self.x - 5, self.y, self.x + 20, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_box())
    def new(self):
        self.x += random.randint(600,1000)
    def update(self):
        self.x = self.x - 7
        if self.x < 20:
            self.x = 800
    def draw(self):
        self.image.clip_draw(0, 0, 90, 90, self.x, self.y)

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_box()
    left_b, bottom_b, right_b, top_b = b.get_box()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

class Boy:

    global x, score, stage, run

    def __init__(self):
        self.x, self.y = 70, 70
        self.frame = 0
        self.time = 0
        self.speed = 10
        self.time2 = 0
        self.image = load_image('Resource/animation_sheet0.png')
        self.dir = 1
        self.state = 0
        self.jumpstate = 0
        x = self.x

    def get_box(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_box())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.jumpstate == 0:
                self.jumpstate = 1
                self.time = 0
            elif self.jumpstate == 1:
                self.jumpstate = 2
                self.time2 = 0

    def update(self):
        global stage, score, run
        self.frame = (self.frame + 1) % 8
        if score > 100 and self.state == 0:
            run = 1
            self.x += speed
            if self.x >= 700:
                self.jumpstate = 0
                stage += 1
                run = 0
                self.x = 735
                self.y = 70
                self.state = 1
        if score > 250 and self.state == 1:
            run = 1
            self.y += speed
            if self.y >= 500:
                self.jumpstate = 0
                self.y = 535
                self.x = 735
                run = 0
                stage += 1
                self.state = 2
        if score > 350 and self.state == 2:
            run =1
            self.x -= speed
            if self.x <= 100:
                self.jumpstate = 0
                self.x = 70
                self.y = 535
                run = 0
                stage += 1
                self.state = 3
        if score > 500 and self.state == 3:
            run =1
            self.y -= speed
            if self.y <= 100:
                self.jumpstate = 0
                self.y = 75
                self.x = 70
                run = 0
                stage += 1
                self.state = 0
        self.jump()
    def jump(self):
        self.time = self.time + 1
        self.time2 = self.time2 + 1
        if self.state == 0:
            if self.y < 70:
                self.y = 70
                self.jumpstate = 0
            if self.jumpstate == 1:
                self.y = self.y + 35 - 9*self.time/2
                if self.y < 70:
                    self.y = 70
                    self.jumpstate = 0
            if self.jumpstate == 2:
                self.y = self.y + 35 - 9*self.time2/2
                if self.y < 70 :
                    self.y = 70
                    self.jumpstate = 0
        if self.state == 1:
            if self.x > 735:
                self.x = 735
                self.jumpstate = 0
            if self.jumpstate == 1:
                self.x = self.x - 35 + 9*self.time/2
                if self.x > 735:
                    self.x = 735
                    self.jumpstate = 0
            if self.jumpstate == 2:
                self.x = self.x - 35 + 9*self.time2/2
                if self.x > 735:
                    self.x = 735
                    self.jumpstate = 0
        if self.state == 2:
            if self.y > 535:
                self.y = 535
                self.jumpstate = 0
            if self.jumpstate == 1:
                self.y = self.y - 35 + 9*self.time/2
                if self.y > 535:
                    self.y = 535
                    self.jumpstate = 0
            if self.jumpstate == 2:
                self.y = self.y - 35 + 9*self.time2/2
                if self.y > 535:
                    self.y = 535
                    self.jumpstate = 0
        if self.state == 3:
            
    def draw(self):
        if self.state != 4:
            self.image.clip_draw((self.frame * 100), (self.state* 100), 100, 100, self.x, self.y)
def enter():
    global boy, wall, back, team,life, bgm, font, team1
    boy = Boy()
    life = Life()
    wall = Wall()
    back = Background()
    team1 = [Object2() for i in range(2)]
    team = [Object() for i in range(3)]
    bgm = load_music('Nomplay.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    pass

def exit():
    global boy, wall, back, life, team,bgm,team1
    del(boy)
    del(bgm)
    del(team)
    del(life)
    del(wall)
    del(back)
    del(team1)
    score = 0
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    global Box, life, game_framework
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_TAB:
            if Box == 0:
                Box = 1
            else:
                Box = 0
        else:
            boy.handle_event(event)

    pass

def update():
    global score, font, bgm, Box, game_framework, life, boy

    if life.switch < 1:
        game_framework.quit()

    if Box == 1:
        score += 1
    else:
        score += 2
    boy.update()
    back.update()
    for Object2 in team1:
        Object2.update()
    for Object in team:
        Object.update()
    pass

def draw():
    global score,font,bgm,Box, run

    clear_canvas()
    back.draw()
    wall.draw()
    life.draw()
    boy.draw()
    if run == 0:
        for Object in team:
            if collide(boy, Object) == False:
                Object.draw()
                if (Box == 1):
                    Object.draw_bb()
            else:
                if life.switch != 0:
                    life.switch -= 1
                Object.new()

        for Object2 in team1:
            if collide(boy,Object2) == False:
                Object2.draw()
                if Box == 1:
                    Object2.draw_bb()
            else:
                if life.switch != 0:
                    life.switch -= 1
                Object2.new()
    if Box == 1:
        boy.draw_bb()
    if font == None:
        font = load_font('Resource\ENCR10B.TTF')
    if (Box == 1):
        font.draw(350,450 ,'Easy')
    else:
        font.draw(350,450, 'Hard')

    font.draw(350,375,'Stage : %d' % (stage + 1))
    font.draw(350,350, 'Score : %d' % score)

    update_canvas()
    delay(0.06 + Box*0.02)
    pass