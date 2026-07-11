import pygame
from entities.player import playr
from settings import screen_length, screen_width, title, fps

plr1=playr(200, 100)

pygame.init()
screen=pygame.display.set_mode((screen_length, screen_width))
pygame.display.set_caption(f"{title}")

running=True
clock=pygame.time.Clock()

while running:
    clock.tick(fps)

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

    plr1.update()

    screen.fill((50,120,255))
    plr1.draw(screen)
    pygame.display.flip()
    

