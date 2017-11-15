import json
from pico2d import *

class TileBackground:
    SCROLL_SPEED_PPS = 10
    def __init__(self, filename):
        f = open(filename)
        self.map = json.load(f)
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        image_filename = self.map['tilesets'][0]['image']
        self.image = load_image(image_filename)
        tileset = self.map['tilesets'][0]
        self.w = tileset['tilewidth'] * self.map['width']
        self.x = tileset['tileheight'] * self.map['height']

    def draw(self):
        tile_per_line = self.map['width']
        map_height = self.map['height']
        map_width = self.map['width']
        data = self.map['layers'][0]['data']
        tileset = self.map['tilesets'][0]
        tile_width = tileset['tilewidth']
        tile_height = tileset['tileheight']
        margin = tileset['margin']
        spacing = tileset['spacing']
        columns = tileset['columns']

        rows = -(-tileset['tilecount'] // columns) # math.ceil()

        startx = tile_width // 2 - self.window_left % tile_width
        starty = tile_height // 2 - self.window_bottom % tile_height

        endx = self.canvas_width + tile_width // 2
        endy = self.canvas_height + tile_height // 2

        desty = starty
        my = int(self.window_bottom // tile_height)
        while(desty < endy):
            destx = startx
            mx = int(self.window_left // tile_width)
            while(destx < endx):
                index = (map_height - my - 1) * map_width - mx
                tile = data[index]
                tx = (tile - 1) % columns
                ty = rows - (tile - 1) // columns - 1
                srcx = margin + tx * (tile_width + spacing)
                srcy = margin + ty * (tile_height + spacing)
                self.image.clip_draw(srcx, srcy, tile_width, tile_height, destx, desty)
                destx += tile_width
                mx += 1
            desty += tile_height
            my += 1

    def set_center_object(self, boy):
        self.center_object = boy


    def update(self, frame_time):
        self.window_left = clamp(0,
            int(self.center_object.x)- self.canvas_width//2,
            self.w - self.canvas_width)
        self.window_bottom = clamp(0,
            int(self.center_object.y)- self.canvas_height//2,
            self.x - self.canvas_height)


    def handle_event(self, event):