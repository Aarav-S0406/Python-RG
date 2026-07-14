import pygame
from entities.player import playr
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG, BLACK, TILE_SIZE

class world():
    def __init__(self, screen):
        self.create_map()
        self.grass = pygame.image.load('assets/images/grass.png').convert_alpha()
        self.grass = pygame.transform.scale(self.grass, (TILE_SIZE, TILE_SIZE))
        self.dirt = pygame.image.load('assets\images\dirt.png').convert_alpha()
        self.dirt = pygame.transform.scale(self.dirt, (TILE_SIZE, TILE_SIZE))
        self.screen=screen
        self.scale=4

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
            [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
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
            for column_index, column in enumerate(row):

                world_x = TILE_SIZE * column_index
                world_y = TILE_SIZE * row_index
                screen_x = world_x - camera.x
                screen_y = world_y - camera.y

                if column==1:
                    screen.blit(self.dirt, (screen_x, screen_y))
                
                elif column==0:
                    screen.blit(self.grass, (screen_x, screen_y))
