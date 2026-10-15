import pygame
from settings import PLAYER_HEIGHT, PLAYER_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_SPEED, BLACK

class playr():
    def __init__(self, screen):
        self.speed=PLAYER_SPEED
        self.x = SCREEN_WIDTH//2   #spawn coord
        self.y = SCREEN_HEIGHT//2
        self.screen=screen
        self.sprite_paths = {
            "idle_down": "assets/Sprites/Entities/Characters/Body_A/Animations/Idle_Base/Idle_Down-Sheet.png",
            "idle_up": "assets/Sprites/Entities/Characters/Body_A/Animations/Idle_Base/Idle_Up-Sheet.png",
            "idle_side": "assets/Sprites/Entities/Characters/Body_A/Animations/Idle_Base/Idle_Side-Sheet.png",
            "walk_down": "assets/Sprites/Entities/Characters/Body_A/Animations/Walk_Base/Walk_Down-Sheet.png",
            "walk_up": "assets/Sprites/Entities/Characters/Body_A/Animations/Walk_Base/Walk_Up-Sheet.png",
            "walk_side": "assets/Sprites/Entities/Characters/Body_A/Animations/Walk_Base/Walk_Side-Sheet.png"
        }
        self.sheet = pygame.image.load(self.sprite_paths).convert_alpha() #sprite
        self.width = 32  #sprite dimensions
        self.height = 32
        self.collision_width = 18
        self.collision_height = 12
        self.scale = 1.3   #sprite scale
        self.color = BLACK
        self.direction = 0
        #animation
        self.frame = 0   #tracks frame number of each animation
        self.action = 0  #switches between different player action sprites
        self.last_update = pygame.time.get_ticks()
        self.animation_list = []
        self.animation_steps = [6,6,6,6,4,4,4] #total number of frames per animation
        self.animation_cooldown = 150
        self.step_counter=0
        self.load_animation()


    # Get Sprite 
    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*width), (self.action*32), width, height))
        image=pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)

        return image

    
    # Animation
    def load_animation(self):
        
        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self.get_image(self.step_counter, 32, 32, self.scale, BLACK))
                self.step_counter+=1
            self.animation_list.append(temp_img_list)

    def get_rect(self):
        return pygame.Rect(
        self.x + (self.width * self.scale - self.collision_width) // 2,
        self.y + (self.height * self.scale - self.collision_height),
        self.collision_width,
        self.collision_height
    )

    def input(self):
        pass

    def movement(self, world):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_w]:
            self.action = 5
            self.direction = 1
            dy = -self.speed

        elif keys[pygame.K_s]:
            self.action = 3
            self.direction = 2
            dy = self.speed

        elif keys[pygame.K_a]:
            self.action = 4
            self.direction = 3
            dx = -self.speed

        elif keys[pygame.K_d]:
            self.action = 4
            self.direction = 4
            dx = self.speed

        else:
            if self.action <= 0:
                self.action = 0
                self.direction = 
            else:
                self.action -= 2

        # -------------------------
        # X MOVEMENT
        # -------------------------

        self.x += dx

        player_rect = self.get_rect()

        for collision in world.collision_rects:

            if player_rect.colliderect(collision):

                if dx > 0:
                    self.x -= player_rect.right - collision.left

                elif dx < 0:
                    self.x += collision.right - player_rect.left

                player_rect = self.get_rect()

        # -------------------------
        # Y MOVEMENT
        # -------------------------

        self.y += dy

        player_rect = self.get_rect()

        for collision in world.collision_rects:

            if player_rect.colliderect(collision):

                if dy > 0:
                    self.y -= player_rect.bottom - collision.top

                elif dy < 0:
                    self.y += collision.bottom - player_rect.top

                player_rect = self.get_rect()

            
    def animate(self):
        
        current_time=pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0

    # Boundary conditions
    def boundary(self):
        
        if self.x<0:
            self.x=0
        if self.x > SCREEN_WIDTH-PLAYER_WIDTH:
            self.x = SCREEN_WIDTH-PLAYER_WIDTH
        if self.y < 0:
            self.y = 0
        if self.y > SCREEN_HEIGHT-PLAYER_HEIGHT:
            self.y = SCREEN_HEIGHT-PLAYER_HEIGHT

    def draw(self, screen, camera):
        screen.blit(self.image, (self.x-camera.x, self.y-camera.y))

    def update(self):
        # self.boundary()
        self.image=self.get_image(
            self.frame,
            self.width,
            self.height,
            self.scale,
            self.color
        )   
        self.animate()
        
        
