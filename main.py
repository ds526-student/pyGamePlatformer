import pygame
import sys
import character

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

x_position = 100
y_position = 100

character_image_path = "assets/player/character.png"  # Update with your image path
player_character = character.Character(x_position, y_position, character_image_path)
standing_image_path = pygame.transform.scale(pygame.image.load("assets/ground/grass.png"), (50, 50))  # Update with your image path

pygame.display.set_caption("Simple Pygame Window")
clock = pygame.time.Clock()

def handleMovement():
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_a]:
        dx -= 1
    if keys[pygame.K_d]:
        dx += 1
    # if keys[pygame.K_w]:
    #     dy -= 1
    # if keys[pygame.K_s]:
    #     dy += 1
    if dx != 0 or dy != 0:
        player_character.move(dx, dy)

def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # generate the environment
        screen.fill((100, 100, 100))
        player_character.draw(screen)

        # game logic
        handleMovement()

        # update the display
        pygame.display.update()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game()