import pygame
from entities.player import playr
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG
from world.terrain import world
from world.tiles import TileManager
from camera import Camra

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"{TITLE}")

tile_manager = TileManager("assets/World/Map.tmx")
cmr1=Camra()
plr1 = playr(screen)

map=world("assets/World/Map.tmx", 
          screen, 
          tile_manager
)

running=True
clock=pygame.time.Clock()



while running:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_e:
                print("E pressed")


        # TODO: Detect E key pressed here

    # 2. UPDATE
    # TODO: Find the current interactable target here

    screen.fill(BG)

    cmr1.update(plr1)
    plr1.update()

    map.draw_layers(screen, cmr1, map.background_layers)
    plr1.draw(screen, cmr1)
    map.draw_layers(screen, cmr1, map.foreground_layers)

    plr1.movement(map)

    # 4. DRAW UI
    # TODO: Draw "E - Interact" prompt here

    pygame.display.flip()