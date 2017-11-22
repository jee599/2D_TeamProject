from pico2d import*

class BackGround:
    SCROLL_SPEED_PPS = 70
    image = None
    def __init__(self,w,h):
        if self.image == None :
            BackGround = load_image("background.pnp")
        self.speed = 0
        self.left = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        x = int(self.self)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x,0,w, self.screen_height,0,0)
        self.image.clip_draw_to_origin(0,0,self.screen_width - w,self.screen_height.w,0)
    def update(self, frame_time):
        self.left = (self.left+frame_time * self.speed) % self.image.w

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.speed -= BackGround.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT:
                self.speed += BackGround.SCROLL_SPEED_PPS
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                self.speed += BackGround.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT:
                self.speed -= BackGround.SCROLL_SPEED_PPS
