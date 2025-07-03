import pygame

class LevelOne:
    def __init__(self):
        self.grass_image_path = pygame.image.load("assets/environment/ground/grass.png").convert()  # Update with your image path

    platforms = [
        # Define platforms here if needed
        pygame.Rect(0, 562, 800, 50),  # Ground platform
        # Example: pygame.Rect(x, y, width, height)
        pygame.Rect(100, 400, 200, 20),
        pygame.Rect(400, 300, 150, 20),
        pygame.Rect(600, 200, 250, 20),
    ]