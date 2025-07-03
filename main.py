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
y_position = 512

# player character set up
player_character = character.Character(x_position, y_position)

pygame.display.set_caption("Simple Pygame Window")
clock = pygame.time.Clock()

def oneLevel():
    levelOne = level_one.LevelOne()
    grass_image = levelOne.grass_image_path

    # generate the environment
    screen.fill((100, 100, 100))
    resized_grass = pygame.transform.scale(grass_image, (level_one.LevelOne.platforms[0][2], level_one.LevelOne.platforms[0][3])) 
    screen.blit(resized_grass, (level_one.LevelOne.platforms[0][0], level_one.LevelOne.platforms[0][1]))  # Draw the ground
    
    resized_grass = pygame.transform.scale(grass_image, (200, 50))
    screen.blit(resized_grass, (level_one.LevelOne.platforms[1][0], level_one.LevelOne.platforms[1][1]))
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