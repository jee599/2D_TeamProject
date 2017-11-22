import random
import json
import os
import Resource

from pico2d import *

import game_framework
import title_state

name = "MainState"

boy = None
grass = None
font = None

def handle_events():
    global running
    events = get_events()

class Back:
    def __init__(self):
        self.frame = 0
        self.image = load_image('Resource/Prison.png')
    def draw(self):
        x = int(self.left)
        w = min(self.iamge.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x,0,w,self.screen_height,0,0)
        self.image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,0)

    def update(self):
        self.frame = (self.frame + 1)
        self.left = (self.left + self.frame * self.speed) % self.image.w

class Object:
    def __init__(self):
        self.image = load_image('Resource/bat1.png')
        self.frame = 0
        self.x = random.randint(0,100)
        self.speed = 5
        self.x + 700
        self.y = random.randint(1,7)

    def update(self):
        self.frame = (self.frame + 1)%6
        self.x = self.x - self.speed
        if self.x <  70:
            self.x = 800
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 90, 90, self.x, self.y*100)

class Grass:
    def __init__(self):
        self.image = load_image('Resource/grass2.png')
        self.frame = 0
    def update(self):
        self.frame = (self.frame + 1)%8
    def draw(self):
        self.image.clip_draw(self.frame *100, 0, 800, 70 ,400, 30)


def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get.bb()

    if left_a > right_b: return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

class Boy:

    global x
    def __init__(self):
        self.x, self.y = 70, 95
        self.frame = 0
        self.time = 0
        self.time2 = 0
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
        self.frame = (self.frame + 1) % 8
        self.time = self.time + 1
        self.time2 = self.time2 + 1
        if self.y < 95:
            self.y = 95
            self.state = 0

        if self.state == 1:
            self.y = self.y + 20 - 9.8*self.time/5
            if self.y < 95:
                self.y = 95
                self.state = 0
        if self.state == 2:
            self.y = self.y + 20 - 9.8*self.time2/3
            if self.y < 95 :
               self.y = 95
               self.state = 0
    def draw(self):
        self.image.clip_draw((self.frame * 100), 0, 100, 100, self.x, self.y)

def enter():
    global boy, grass, back, team
    boy = Boy()
    grass = Grass()
    back = Back()
    team = [Object() for i in range(6)]
    pass

def exit():
    global boy, grass, back
    del(boy)
    del(grass)
    del(back)
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.chage_state(title_state)
        else:
            boy.handle_event(event)

    pass

def update():
    boy.update()
    back.update()
    grass.update()
    for Object in team:
        Object.update()
    pass

def draw():
    clear_canvas()
    back.draw()
    boy.draw()
    boy.draw_bb()
    grass.draw()
    for Object in team:
        Object.draw()
    update_canvas()
    delay(0.09)
    pass