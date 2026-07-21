import pygame
from entities.player import playr
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG, BLACK, TILE_SIZE, GRASS, ROCK, DIRT

class world():
    def __init__(self, screen):
        self.create_map()
        self.world_x=0
        self.world_y=0
        self.tiles={
            GRASS : {
                "image" : pygame.image.load('assets/images/grass.png').convert_alpha(),
                "solid" : False
            },
            DIRT : {
                "image" : pygame.image.load('assets/images/dirt.png').convert_alpha(),
                "solid" : False
            },
            ROCK : {
                "image" : pygame.image.load('assets/images/Rock.png').convert_alpha(),
                "solid" : True
            }
        }
        
        # self.grass = pygame.transform.scale(self.grass, (TILE_SIZE, TILE_SIZE))
        # self.dirt = pygame.transform.scale(self.dirt, (TILE_SIZE, TILE_SIZE))
        # self.rock = pygame.transform.scale(self.rock, (TILE_SIZE, TILE_SIZE))
        self.screen=screen

    def create_map(self):
        self.world = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,3,0,0,1,0,0,0,3,0,0,0,1,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]

    def draw(self, screen, camera):
        for row_index, row in enumerate(self.world):
            for column_index, tile in enumerate(row):

                self.world_x = TILE_SIZE * column_index
                self.world_y = TILE_SIZE * row_index
                screen_x = self.world_x - camera.x
                screen_y = self.world_y - camera.y
              
                screen.blit(self.tiles[tile]["image"], (screen_x, screen_y))
    
    def collision(self):
        if self.tiles["solid"]:
            print("1")
        self.world_y
        pass