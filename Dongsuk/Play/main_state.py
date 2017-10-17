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

class Back:
    def __init__(self):
        self.image = load_image('Resource/Prison.png')
    def draw(self):
        self.image.draw(400,300)

class Grass:
    def __init__(self):
        self.image = load_image('Resource/grass2.png')
        self.frame = 0
    def update(self):
        self.frame = (self.frame + 1)%8
    def draw(self):
        self.image.clip_draw(self.frame *100, 0, 800, 70 ,400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 50, 90
        self.frame = 0
        self.image = load_image('Resource/animation_sheet.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw((self.frame * 100), 0, 100, 100, self.x, self.y)

def enter():
    global boy, grass, back
    boy = Boy()
    grass = Grass()
    back = Back()
    pass

def exit():
    global boy, grass
    del(boy)
    del(grass)
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

    pass

def update():
    boy.update()
    grass.update()
    pass

def draw():
    clear_canvas()
    back.draw()
    boy.draw()
    grass.draw()
    update_canvas()
    delay(0.09)
    pass