import pygame

diagMove = 0.7071 # 1 / sqrt(2)

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, velocity_x=5):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_x = velocity_x

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, dx, dy):
        # Normalize for diagonal movement
        if dx != 0 and dy != 0:
            dx *= diagMove
            dy *= diagMove
        self.rect.x += int(dx * self.velocity)
        self.rect.y += int(dy * self.velocity)
