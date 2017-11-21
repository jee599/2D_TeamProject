import game_framework
import pico2d import*

class Button:
    font = None
    def __init__(self,imageFilename, hoverFilename = None, x= 0, y = 0):
        self.image = load_iamge(imageFilename)
        if(hoverFilename == None):
            self.hoverImage = None
        else :
            self.hoverImage = load_image(hoverFilename)
        self.x, self.y = x,y
        self.hover = False
        self.text = ""
        if(Button.font == None):
            Button.font = load_font()
    def draw(self):
        image = self.image if self.hover else self.Image
        image.draw(self.x, self.y)
        if(self.text!="")
            w = len(self.text) * 10
            h = 30
            x = self.x - w/2
            y = self.y - h / 2
            self.font.draw(x,y,self.text)
    def handle_event(self,event):
        if event.type == SDL_MOUSEMOTION:
            if(self.hoverImage != None):
                self.hover = self.ptinRect(event.x, event.y)
        if event.type == SDL_MOUSEBOTTONDOWN:
            if ptinRect(MouseXY,myRect):
                self.onOver()
            else:
                button.handle_event(event)
    def ptinRect(self,x,y):
        if(x < self.x - self.image.w / 2):
            return False
        if(x > self.x + self.image.w / 2):
            return False
        if(y < self.y - self.image.h / 2 ):
            return False
        if(y > self.y + self.image.h / 2):
            return False
        return True

def add(obj):
    ui_object_append(obj)
def handle_event(event):
    for obj in ui_objects:
        obj.handle_event(event)

def draw():
    for obj in ui_object:
        obj.draw()