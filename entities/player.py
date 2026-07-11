import pygame
from settings import PLAYER_HEIGHT, PLAYER_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_SPEED, BLACK

class playr():
    def __init__(self, image):
        self.speed=PLAYER_SPEED
        self.x=10   #spawn coord
        self.y=10
        self.sheet=image #sprite
        #animation
        self.frame=0
        self.action=0
        self.last_update = pygame.time.get_ticks()
        self.animation_list = []
        self.animation_steps = [6,6,6,6]
        self.animation_cooldown = 150
        self.step_counter=0



    # Get Sprite 
    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*width), 128, width, height))
        image=pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)

        return image
    
    # Animation
    def load_animation(self):
        
        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self.get_image(self.step_counter, 32, 31, 3, BLACK))
                self.step_counter+=1
            self.animation_list.append(temp_img_list)

    #     screen.blit(self.image, (self.x, self.y))
    #     pygame.draw.rect(
    #         screen,
    #         (0,255,0),
    #         (self.rect, 2)
    #     )

    def input(self):
        pass

    def movement(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_w]:
            pass
        if keys[pygame.K_s]:
            self.y+=self.speed
        if keys[pygame.K_a]:
            self.x-=self.speed
        if keys[pygame.K_d]:
            pass

    def animate(self):
        
        current_time=pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
        if self.frame >= len(self.animation_list):
            self.frame = 0

    # Boundary conditions
    def boundary(self):
        
        if self.x<0:
            self.x=0
        if self.x > SCREEN_HEIGHT-PLAYER_HEIGHT:
            self.x= SCREEN_HEIGHT-PLAYER_HEIGHT
        if self.y< 0:
            self.y= 0
        if self.y > SCREEN_WIDTH-PLAYER_WIDTH:
            self.y= SCREEN_WIDTH-PLAYER_WIDTH

    def update(self):
        self.load_animation()
        self.movement()
        self.animate()
        self.boundary()
