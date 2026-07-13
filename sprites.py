import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet=image
 
    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*width), 128, width, height))
        image=pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)

        return image
  
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BG = (50,50,50)
BLACK = (0,0,0)

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('spritesheets')

sprite_sheet_image = pygame.image.load("assets/images/Player.png").convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)

# create animation list
animation_list = []
animation_steps = [6,6,6,6]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0
step_counter=0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 32, 31, 3, BLACK))
        step_counter+=1
    animation_list.append(temp_img_list)

run=True
while run:

    #update background
    screen.fill(BG)

    #display image
    #screen.blit(sprite_sheet_image, (0,0))

    #update animation
    current_time=pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    #show image
    screen.blit(animation_list[action][frame], (0, 0))

    #event handeler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0
    
    pygame.display.update()

pygame.quit() 