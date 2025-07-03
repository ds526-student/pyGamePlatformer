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
                 character_image_path="assets/player/character.png", # the location of the player image 
                 velocity_x=veocityX, # horizontal speed
                 velocity_y=velocityY, # vertical speed
                 jump_height=jumpHeight, # the height of the jump
                 jumping=False, # whether the character is currently jumping or not
                ):
        
        super().__init__()
        self.image = pygame.image.load(character_image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
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

    def check_collisions(self, platforms):
        # check collisions with every platform
        for platform in platforms:
            if self.rect.colliderect(platform):
                # If player is falling and hits a platform from above
                if self.velocity_y <= 0 and self.rect.bottom <= platform.top + 10:
                    self.rect.bottom = platform.top
                    self.jumping = False
                    self.velocity_y = 0
                else:
                    # Push player out of platform horizontally
                    if self.rect.centerx < platform.centerx:
                        self.rect.right = platform.left
                    else:
                        self.rect.left = platform.right