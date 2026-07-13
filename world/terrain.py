import pygame
from entities.player import playr
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG, BLACK

class world():
    def __init__(self, screen):
        self.world = world
        self.grass = pygame.image.load('assets/images/grass.png').convert_alpha()
        self.dirt = pygame.image.load('assets\images\dirt.png').convert_alpha()
        self.screen=screen

    def load_tiles(self):
        dirt = pygame.Surface((16, 16)).convert_alpha()
        dirt.blit(self.dirt, (0, 0), (16, 16, 16, 16))
        #dirt=pygame.transform.scale(dirt, (48, 48))

        grass = pygame.Surface((16, 16)).convert_alpha()
        grass.blit(self.dirt, (0, 0), (16, 16, 16, 16))
        #grass=pygame.transform.scale(grass, (48, 48))
        #image.set_colorkey(color)

    def create_map(self):
        self.world=[
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0],
            [0,0,0,0,0]
        ]

    def draw(self, screen):
        for x in range(int(world)):
            for y in x:
                if y==0:
                    screen.blit(self.dirt, (x, y))
                
                elif y==1:
                    screen.blit(self.grass, (x, y))





