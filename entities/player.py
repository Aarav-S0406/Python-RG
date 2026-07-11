import pygame
from settings import player_height, player_width, screen_length, screen_width, player_speed

class playr(pygame.sprite.Sprite):
    def __init__(self, dx, dy):
        super().__init__()
        
        self.speed=player_speed
        raw_image=pygame.image.load(r"assets\images\Player.png").convert_alpha()
        self.image=pygame.transform.scale(raw_image, (player_width, player_height))
        self.rect=self.image.get_rect()
        self.rect.x=dx
        self.rect.y=dy

    def update(self):

        keys=pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y-=self.speed
        if keys[pygame.K_s]:
            self.y+=self.speed
        if keys[pygame.K_a]:
            self.x-=self.speed
        if keys[pygame.K_d]:
            self.x+=self.speed
    
        if self.x<0:
            self.x=0
        if self.x > screen_length-player_height:
            self.x= screen_length-player_height
        if self.y< 0:
            self.y= 0
        if self.y > screen_width-player_width:
            self.y= screen_width-player_width

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(
            screen,
            (0,255,0),
            (self.rect, 2)
)

player1=playr(200, 100)