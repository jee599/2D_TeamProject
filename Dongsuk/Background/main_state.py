from pico2d import*
#import title_state
import game_framework
import random
import numbers


class Background:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.speed = 0
        self.image = load_image('background.png')
    def draw(self):
        x=int(self.left)
        w=min(self.image.w-x, self.screen_width)
        self.image.clip_draw_to_origin(x,0,w,self.screen_height,0,0)
        self.image.clip_draw_to_origin(0,0, self.screen_width-w, self.screen_height, w,0)

    def update(self, frame_time):
        self.left = (self.left + frame_time * self.speed) % self.image.w

class Grass:
    bgm = None
    def __init__(self):
        self.image= load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)
        if grass.bgm == None:
            grass.bgm = load_music('football.mp3')
            grass.bgm.set_volume(100)
            grass.bgm.repeat_play()


class Boy:
    image = None
    eat_sound = None
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')
        if Boy.eat_sound == None:
            Boy.eat_sound = load_wav('pickup.wav')
            Boy.eat_sound.set_volume(32)

    def eat(self):
        self.eat_sound.play()

    def draw(self):
        self.image.clip_draw(self.frame*100, self.state * 100, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x -50, self.y -50, self.x + 50, self.y +50

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 280:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 140:
            self.state = self.LEFT_RUN
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 280:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 140:
            self.state = self.RIGHT_RUN
            self.run_frames = 0

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

    def mouse_update(self):
        self.frame = (self.frame + 1) % 8
        if team[boyNum].state == self.RIGHT_RUN:
            team[boyNum].x = min(800, self.x + 5)
        elif team[boyNum].state == self.LEFT_RUN:
            team[boyNum].x = max(0, self.x - 5)
        elif team[boyNum].state == self.RIGHT_STAND:
            team[boyNum].stand_frames += 1
        elif team[boyNum].state == self.LEFT_STAND:
            team[boyNum].stand_frames += 1



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global boy, grass, team, boyNum, mouseX, mouseY
    boy = Boy()
    grass = Grass()
    team = [Boy() for i in range(11)]
    boyNum = 0
    mouseX = 0
    mouseY = 0



def exit():
    global boy, grass, team, boyNum,  mouseX, mouseY
    del(boy)
    del(grass)
    del(team), (boyNum)
    del(mouseX), (mouseY)


def handle_events():
    global mouseX
    global mouseY
    global boyNum

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:\
            game_framework.change_state(title_state)
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                boy.eat()



def update():
    handle_events()
    boy.update()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()

    numbers.draw(boyNum + 1, 740, 540)

    update_canvas()

