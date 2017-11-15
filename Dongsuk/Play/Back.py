import json
from pico2d import *

class TileBackground:
    SCROLL_SPEED_PPS = 10
    def __init__(self, Filename, Width, Height):
        f = open(Filename)
        self.map = json.load(f)
        self.x,self.y = 0,0
        self.canvasWidth = Width
        self.canvasHeight = Height
        image_filename = self.map['tilesets'][0]['image']
        self.image = load_image(image_filename)
        self.speedx,self.speedy = 0,0

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

        startx = tile_width // 2 - self.x % tile_width
        starty = tile_height // 2 - self.y % tile_height

        endx = self.canvasWidth + tile_width // 2
        endy = self.canvasHeight + tile_height // 2

        desty = starty
        my = int(self.y // tile_height)
        while(desty < endy):
            destx = startx
            mx = int(self.x // tile_width)
            while(destx < endx):
                index = (map_height - my - 1) * map_width - mx
                tile = data[index]
                tx = (tile - 1) % columns
                ty = rows - (tile - 1) // columns - 1
                srcx = margin + tx * (tile_width + spacing)
                srcy = margin + ty * (tile_height + spacing)
                self.image.clip_draw(srcx, srcy, tile_width, tile_height, destx + self.speedx, desty)
                destx += tile_width
                mx += 1
            desty += tile_height
            my += 1