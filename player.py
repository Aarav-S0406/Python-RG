import pygame

p_length=40
p_width=60
s_length=800
s_width=600

class playr:
    def __init__(self, dx, dy):
        self.x=dx
        self.y=dy
        self.speed=10

    def update(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y-=self.speed
        if keys[pygame.K_s]:
            self.y+=self.speed
        if keys[pygame.K_a]:
            self.x-=self.speed
        if keys[pygame.K_d]:
            self.x+=self.speed
    
        if self.x<0:
            self.x=0
        if self.x > s_length-p_length:
            self.x= s_length-p_length
        if self.y< 0:
            self.y= 0
        if self.y > s_width-p_width:
            self.y= s_width-p_width

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (0,255,0),
            (self.x, self.y, p_length, p_width)
)

player1=playr(200, 100)