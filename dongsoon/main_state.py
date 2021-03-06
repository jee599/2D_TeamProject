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
        self.image = load_image('Resource/Prison.png')
    def draw(self):
        self.image.draw(400,300)

class Object:
    def __init__(self):
        self.image = load_image('Resource/bat.png')
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

class Boy:

    global x
    def __init__(self):
        self.x, self.y = 70, 95
        self.frame = 0
        self.time = 0
        self.time2 = 0
        self.image = load_image('Resource/animation_sheet.png')
        self.dir = 1
        self.state = 0
        x = self.x
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
            game_framework.change_state(title_state)
        else:
            boy.handle_event(event)

    pass

def update():
    boy.update()
    grass.update()
    for Object in team:
        Object.update()
    pass

def draw():
    clear_canvas()
    back.draw()
    boy.draw()
    grass.draw()
    for Object in team:
        Object.draw()
    update_canvas()
    delay(0.09)
    pass
