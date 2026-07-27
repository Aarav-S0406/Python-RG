import pygame
import pytmx
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG, BLACK, TILE_SIZE, GRASS, ROCK, DIRT

class world():

    def __init__(self, map_path, screen, TileManager):
        self.map_path=map_path
        self.screen=screen
        self.TileManager=TileManager
        self.load_map()
        # self.is_solid(playr.x, playr.y)


    def load_map(self):
        self.tmx = pytmx.load_pygame(self.map_path)
        self.width=self.tmx.width
        self.height=self.tmx.height
        self.tilewidth=self.tmx.tilewidth
        self.tileheight=self.tmx.tileheight

        
    def draw(self, screen, camera):
        for layer in self.tmx.visible_layers:
            if hasattr(layer, "data"):
                for x,y,gid in layer:
                    if gid == 0:
                        continue

                    world_x = TILE_SIZE * x
                    world_y = TILE_SIZE * y
                    self.screen_x = world_x - camera.x
                    self.screen_y = world_y - camera.y

                    image = self.TileManager.get_image(gid)

                    screen.blit(image, (self.screen_x, self.screen_y))


    def get_gid(world_x, world_y):
        pass


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