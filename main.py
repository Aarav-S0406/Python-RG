import pygame
from entities.player import playr
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG
from world.terrain import world

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"{TITLE}")


plr1 = playr(screen)
map=world(screen)

running=True
clock=pygame.time.Clock()

while running:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

    screen.fill(BG)

    map.draw(screen)

    plr1.update()

    #plr1.draw()
    
    pygame.display.flip()
    

