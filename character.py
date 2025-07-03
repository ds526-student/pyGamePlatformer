import pygame

diagMove = 0.7071 # 1 / sqrt(2)
gravity = 1
veocityX = 7.5
velocityY = 0
jumpHeight = 20
jumping = False

class Character(pygame.sprite.Sprite):
    # Character class for the player character in the game
    def __init__(self,
                 x, # the x position of the player
                 y, # the y position of the player
                 image_path, # the location of the player image 
                 velocity_x=veocityX, # horizontal speed
                 velocity_y=velocityY, # vertical speed
                 jump_height=jumpHeight, # the height of the jump
                 jumping=False, # whether the character is currently jumping or not
                ):
        
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.jumpheight = jump_height
        self.jumping = jumping

    def update(self):
        pass

    # draw the character on the surface
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    # handle the movement of the character
    def handle_movement(self):
        # horizontal movement
        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_a]:
            dx -= 1
        elif keys[pygame.K_d]:
            dx += 1

        self.rect.x += int(dx * self.velocity_x)

        # vertical movement
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.velocity_y = jumpHeight

        if self.jumping:
            self.rect.y -= int(self.velocity_y)
            self.velocity_y -= gravity
            
            if self.velocity_y < -self.jumpheight:
                self.jumping = False
                self.velocity_y = jumpHeight