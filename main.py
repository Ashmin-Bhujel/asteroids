import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


# Entrypoint
def main():
    print("=" * 20)
    print("Starting Asteroids!")
    print("=" * 20)
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")
    print("=" * 20)

    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Asteroids Game")
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    font = pygame.font.Font(None, 32)

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
        score_text = font.render(f"Score: {score}", True, "#111111", "#fafafa")
        screen.blit(score_text, (10, 10))

        # Detect collisions
        for asteroid in asteroids:
            # Between asteroids and player
            if asteroid.is_collided(player):
                print("=" * 20)
                print("Game Over!")
                print(f"Your Score: {score}")
                print("=" * 20)
                sys.exit(1)

            # Between asteroids and shots
            for shot in shots:
                if asteroid.is_collided(shot):
                    score += asteroid.split()
                    shot.kill()

        # Draw all the drawable objects
        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
