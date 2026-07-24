import pygame
from entities.player import playr
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG
from world.terrain import world
from camera import Camra

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"{TITLE}")


cmr1=Camra()
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

    plr1.update()
    cmr1.update(plr1)

    map.draw(screen, cmr1)
    plr1.draw(screen, cmr1)
    plr1.movement(map)
    

    pygame.display.flip()
    

