import pygame
from entities.player import playr
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG

pygame.init()
screen=pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption(f"{TITLE}")

sprite_sheet_image = pygame.image.load('assets/images/Player.png').convert_alpha()
plr1 = playr(sprite_sheet_image)

running=True
clock=pygame.time.Clock()

while running:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

    plr1.update()

    screen.fill(BG)
    
    pygame.display.flip()
    

