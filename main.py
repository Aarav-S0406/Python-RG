import pygame
from player import playr
from player import s_length
from player import s_width

plr1=playr(200, 100)

s_length=800
s_width=600

pygame.init()
screen=pygame.display.set_mode((s_length, s_width))
pygame.display.set_caption("My RPG")

running=True
clock=pygame.time.Clock()

while running:
    clock.tick(60)

    # keys=pygame.key.get_pressed()

    # if keys[pygame.K_w]:
    #     plr1.y-=plr1.speed
    # if keys[pygame.K_s]:
    #     plr1.y+=plr1.speed
    # if keys[pygame.K_a]:
    #     plr1.x-=plr1.speed
    # if keys[pygame.K_d]:
    #     plr1.x+=plr1.speed
    
    # if plr1.x<0:
    #     plr1.x=0
    # if plr1.x > s_length-p_length:
    #     plr1.x= s_length-p_length
    # if plr1.y< 0:
    #     plr1.y= 0
    # if plr1.y > s_width-p_width:
    #     plr1.y= s_width-p_width

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

    plr1.update()

    screen.fill((50,120,255))
    plr1.draw(screen)
    pygame.display.flip()
    

