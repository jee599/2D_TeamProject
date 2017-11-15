import tile_state as main state

class TileBackground:
    def draw(self):
        mapWidth = self.map['width']
        mapHeight = self.map['height']
        data = self.map['layes'][self.layerIndex]['data']
        tileset = self.map['tilests'][0]
        tileWidth = tileset['tilewidth']
        tileHeight = tileset['tileheight']
        margin = tileset['margin']
        spacing = tileset['spacing']
        columns = tileset['columns']
        dx = 0 + tileWidth / 2
        dy = 0 + tileHeight / 2
        desty = dy
        y = 0

        startx = tileWidth // 2 - self.x % tileWidth
        starty = tileHeight // 2 - self.y % tileHeight
        endx = self.canvasWidth + tileWidth // 2
        endy = self.canvasHeight + tileHeight // 2

        desty = starty
        my = int(self.y // tileHeight)
        while(desty < endy):
            destx = startx
            index = (mapHeight -my - 1) *mapWidth +mx
            tile = data[index]
            tx = (tile -1 )% columns
            ty = rows - (tile - 1) // columns - 1
            srcx = margin + tx * (tileWidth + spacing)
            srcy = margin + ty * (tileHeight + spacing)
            self.image.clip.draw(srcx,srcy,tileWidth,tileHeight,destx,desty)
            destx += tileWidth
            mx += 1
    def update(self,frame_time):
        self.left = (self.left + self.speed) % self.tile_map.map_width


