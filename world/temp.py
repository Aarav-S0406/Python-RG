import pytmx
import pygame

tmx=pytmx.load_pygame("assets/World/Map.tmx")

for layer in tmx.visible_layers:
    print(type(layer.data)) 

pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption("TITLE")

running=True
clock=pygame.time.Clock()

while running:

    clock.tick(60)
    for event in pygame.event.get():
    
            if event.type==pygame.QUIT:
                running=False
    