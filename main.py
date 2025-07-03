import pygame
import sys
import character
import level_one

pygame.init()
# window dimensions
width = 800     
height = 600
screen = pygame.display.set_mode((width, height))

# player start position
x_position = 300
y_position = 450

# player character set up
character_image_path = "assets/player/character.png"  # Update with your image path
player_character = character.Character(x_position, y_position, character_image_path)

pygame.display.set_caption("Simple Pygame Window")
clock = pygame.time.Clock()

def oneLevel():
    levelOne = level_one.LevelOne()
    ground_image = levelOne.ground_image_path

    # generate the environment
    screen.fill((100, 100, 100))
    screen.blit(ground_image, (0, height - 50))
    player_character.draw(screen)

def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        oneLevel()

        # game logic
        player_character.handle_movement()

        # update the display
        pygame.display.update()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game()