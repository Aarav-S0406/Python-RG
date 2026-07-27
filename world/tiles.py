import pygame
import pytmx

class TileManager():

    def __init__(self, map_path):
        self.tiles = {}
        self.map_path=map_path
        self.load_tiles()
        self.build_dictionary()
  


    def load_tiles(self):
        self.tmx = pytmx.load_pygame(self.map_path)
        self.width=self.tmx.width
        self.height=self.tmx.height


    def build_dictionary(self):
        count=0
        for layer in self.tmx.visible_layers:
            if hasattr(layer, "data"):
                for x, y, gid in layer:
                    if gid == 0:
                        continue
                    if gid not in self.tiles:
                        self.tiles[gid] = {
                            "image": self.tmx.get_tile_image_by_gid(gid),
                            "properties": self.tmx.get_tile_properties_by_gid(gid)
                        }
                    count+=1
        print(count)

        return self.tiles

    def get_image(self, gid):
        image = self.tiles[gid]["image"]
        return image

    def get_properties(self, gid):
        properties = self.tiles[gid]["properties"]
        return properties

    def is_solid(self, gid):
        return bool(self.tiles[gid]["properties"]["solid"])


# pygame.init()
# pygame.display.set_mode((1, 1))   # Tiny dummy window

# tmx = pytmx.load_pygame("assets/world/Map.tmx")

# tiles = {}

# for layer in tmx.visible_layers:
#     if hasattr(layer, "data"):
#         for x, y, gid in layer:
#             if gid == 0:
#                 continue

#             if gid not in tiles:
#                 tiles[gid] = {
#                     "image": tmx.get_tile_image_by_gid(gid),
#                     "properties": tmx.get_tile_properties_by_gid(gid)
#                 }

# print(tiles)