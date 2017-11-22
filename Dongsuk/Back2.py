from pico2d import*

def create_world():
    global boy, background
    boy = Boy()
    background = Background()

    background.set_center_object(boy)
    boy.set_background(background)

def set_center_object(self,boy):
    self.center_obejct = boy

def draw(self):
    self.image.clip_to_origin(
        self.window_left,self.window_bottom,
        self.canvas_width,self.canvas_height,0,0)

def update(self, frame_time):
    self.window_left = clamp(0,int(self.center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)
    self.window_bottom = clamp(0, int(self.center_object) - self.canvas_height // 2, self.h - self.canvas_height)
