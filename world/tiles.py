import pygame
import pytmx

class TileManager():

    def __init__(self, map_path):
        self.tiles = {}
        self.collision_tiles = {}
        self.collision_rects = []
        self.map_path=map_path
        self.animation_start = pygame.time.get_ticks()
        self.load_tiles()
        self.build_dictionary()
        self.build_collisions()
  


    def load_tiles(self):
        self.tmx = pytmx.load_pygame(self.map_path)
        self.width=self.tmx.width
        self.height=self.tmx.height


    # def build_dictionary(self):
     
    #     for layer in self.tmx.visible_layers:
    #         if hasattr(layer, "data"):
    #             for x, y, gid in layer:
    #                 if gid == 0:
    #                     continue
    #                 if gid not in self.tiles:
    #                     self.tiles[gid] = {
    #                         "image": self.tmx.get_tile_image_by_gid(gid),
    #                         "properties": self.tmx.get_tile_properties_by_gid(gid)
    #                     }
    #     return self.tiles

    
    def build_dictionary(self):

        for layer in self.tmx.visible_layers:
            if hasattr(layer, "data"):
                for x, y, gid in layer:
                    if gid == 0:
                        continue

                    if gid not in self.tiles:
                        properties = (
                            self.tmx.get_tile_properties_by_gid(gid) or {}
                        )

                        self.tiles[gid] = {
                            "image": self.tmx.get_tile_image_by_gid(gid),
                            "properties": properties,
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


    # def get_image(self, gid):
    #     image = self.tiles[gid]["image"]
    #     return image

    
    def get_image(self, gid):  

        tile = self.tiles[gid]
        frames = tile["properties"].get("frames", [])

        # Static tile: return its normal image
        if not frames:
            return tile["image"]

        # Calculate elapsed animation time
        elapsed = pygame.time.get_ticks() - self.animation_start

        # Total duration of one animation cycle
        total_duration = sum(frame.duration for frame in frames)

        if total_duration <= 0:
            return tile["image"]

        # Current position in the animation cycle
        animation_time = elapsed % total_duration

        # Find the frame corresponding to that time
        for frame in frames:
            if animation_time < frame.duration:
                return self.tmx.get_tile_image_by_gid(frame.gid)

            animation_time -= frame.duration

        return self.tmx.get_tile_image_by_gid(frames[0].gid)


    def get_properties(self, gid):
        properties = self.tiles[gid]["properties"]
        return properties

    def is_solid(self, gid):
        return bool(self.tiles[gid]["properties"]["solid"])
