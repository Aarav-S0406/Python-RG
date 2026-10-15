import pygame
import pytmx
from settings import *

class world():

    def __init__(self, map_path, screen, TileManager):
        self.map_path=map_path
        self.screen=screen
        self.TileManager=TileManager
        self.collision_rects = TileManager.collision_rects
        self.load_map()
        self.background_layers = ["Grass", "mountain", "mountain2", "River_and_Lakes", "paths(stone_and_dirt)", "paths2(grass)", "paths(stone and dirt)", 
                                  "vegetation_2", "vegetation_1", "Wooden_Props", "Walls2", "Walls", "decoration", "decoration2",
                                  "tree_trunks_1"]
        self.foreground_layers = ["Roofs", "roofs2", "Rocks", "shadows2", "shadows1", "trees_top_2", "Trees_top_1"]
        # self.is_solid(playr.x, playr.y)


    def load_map(self):
        self.tmx = pytmx.load_pygame(self.map_path)
        self.width=self.tmx.width
        self.height=self.tmx.height
        self.tilewidth=self.tmx.tilewidth
        self.tileheight=self.tmx.tileheight

    def draw_layers(self, screen, camera, layer_order):
        for layer in self.tmx.visible_layers:
            if layer.name not in layer_order:
                continue
        
            if hasattr(layer, "data"):
                                   
                for x in range((camera.x//TILE_SIZE),(camera.x//TILE_SIZE)+52):
                    for y in range((camera.y//TILE_SIZE),(camera.y//TILE_SIZE)+40):
                                    
                        self.world_x = TILE_SIZE * x
                        self.world_y = TILE_SIZE * y
                        self.screen_x = self.world_x - camera.x
                        self.screen_y = self.world_y - camera.y
                        
                        gid = self.get_gid(layer, x, y)
                        if gid == 0:
                            continue
                                            
                        image = self.TileManager.get_image(gid)
                                                
                        screen.blit(image, (self.screen_x, self.screen_y))
            
  
    def get_gid(self, layer, tile_x, tile_y):

        if tile_x < 0 or tile_y < 0:
            return 0

        if tile_y >= len(layer.data):
            return 0

        if tile_x >= len(layer.data[tile_y]):
            return 0
        
        gid = layer.data[tile_y][tile_x]
        return gid


    def is_solid(self, position_x, position_y):

        """
        Returns True if the position is blocked.
        Returns False if it can be walked on.
        """

        # Convert world coordinates to tile coordinates
        tile_col_index = position_x // TILE_SIZE
        tile_row_index = position_y // TILE_SIZE

        # Find which tile is at that position
        tile=self.world[tile_row_index][tile_col_index]

        # Check whether that tile is solid
        state = bool(self.tiles[tile]["solid"])
        print(state)

        # Return the answer
        return state

    def change_map(self, new_map):
        self.map_path = new_map
        self.load_map()
