import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


# Entrypoint
def main():
    print("Starting Asteroids!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Game loop
    while True:
        # Logic to quit the game when clicked the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, "black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
