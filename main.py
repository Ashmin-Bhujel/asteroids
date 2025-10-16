import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


# Entrypoint
def main():
    print("Starting Asteroids!")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Asteroids Game")
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # Game loop
    while True:
        # Logic to quit the game when clicked the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all the updatable objects
        updatable.update(dt)
        screen.fill("#111111")

        # Detect collisions
        for asteroid in asteroids:
            # Between asteroids and player
            if asteroid.is_collided(player):
                print("Game Over!")
                sys.exit(1)

            # Between asteroids and shots
            for shot in shots:
                if asteroid.is_collided(shot):
                    asteroid.kill()
                    shot.kill()

        # Draw all the drawable objects
        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
