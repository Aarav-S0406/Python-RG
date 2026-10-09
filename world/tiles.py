import pygame
import pytmx

class TileManager():

    def __init__(self, map_path):
        self.tiles = {}
        self.collision_tiles = {}
        self.collision_rects = []
        self.map_path=map_path
        self.load_tiles()
        self.build_dictionary()
        self.build_collisions()
  


    def load_tiles(self):
        self.tmx = pytmx.load_pygame(self.map_path)
        self.width=self.tmx.width
        self.height=self.tmx.height


    def build_dictionary(self):
     
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
        return self.tiles

    def build_collisions(self):

        self.collision_rects = []

        # -------------------------
        # Collision 1 - Tile Layer
        # -------------------------

        layer = self.tmx.get_layer_by_name("Collisions1")

        for x, y, gid in layer:

            if gid == 0:
                continue

            rect = pygame.Rect(
                x * self.tmx.tilewidth,
                y * self.tmx.tileheight,
                self.tmx.tilewidth,
                self.tmx.tileheight
            )

            self.collision_rects.append(rect)

        # -------------------------
        # Collision 2 - Object Layer
        # -------------------------

        layer = self.tmx.get_layer_by_name("Collisions2")

        for obj in layer:

            rect = pygame.Rect(
                obj.x,
                obj.y,
                obj.width,
                obj.height
            )

            self.collision_rects.append(rect)

    # def build_collisions(self):

    #     for layer in self.tmx.layers:
    #         print(
    #             layer.name,
    #             type(layer),
    #             hasattr(layer, "data")
    #         )

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


# tmx = pytmx.load_pygame("assets/World/Map.tmx")
# for layer in tmx.visible_layers:
#     print(type(layer.data))