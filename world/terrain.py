import pygame
import pytmx
#from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG, BLACK, TILE_SIZE, GRASS, ROCK, DIRT, 
from settings import *

class world():

    def __init__(self, map_path, screen, TileManager):
        self.map_path=map_path
        self.screen=screen
        self.TileManager=TileManager
        self.collision_rects = TileManager.collision_rects
        self.load_map()
        # self.is_solid(playr.x, playr.y)


    def load_map(self):
        self.tmx = pytmx.load_pygame(self.map_path)
        self.width=self.tmx.width
        self.height=self.tmx.height
        self.tilewidth=self.tmx.tilewidth
        self.tileheight=self.tmx.tileheight

    def draw_layers(self, screen, camera, layer_order):
        pass
        
    def draw(self, screen, camera):
        for layer in self.tmx.visible_layers:
            print(layer.name)
            if layer.name == "Grass":


            # if layer.name == "Collisions1":
            #     continue
        
            if hasattr(layer, "data"):
                   
                for x in range((camera.x//TILE_SIZE),(camera.x//TILE_SIZE)+52):
                     for y in range((camera.y//TILE_SIZE),(camera.y//TILE_SIZE)+40):
                # for x in range((camera.x//TILE_SIZE),(self.screen_x//TILE_SIZE)+52):
                #     for y in range((camera.y//TILE_SIZE),(self.screen_y//TILE_SIZE)+40):

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
