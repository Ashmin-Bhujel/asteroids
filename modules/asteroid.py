import random
import pygame
from constants import ASTEROID_MIN_RADIUS
from modules.circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#fafafa", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # Return 1 if it is a small asteroid
        if self.radius == ASTEROID_MIN_RADIUS:
            return 1

        # Get a random angle between 20 and 50
        random_angle = random.uniform(20, 50)

        # Create new velocity and radius for two new child asteroids
        first_child_velocity = self.velocity.rotate(random_angle)
        second_child_velocity = self.velocity.rotate(-random_angle)
        child_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new child asteroids
        first_child = Asteroid(self.position.x, self.position.y, child_asteroid_radius)
        second_child = Asteroid(self.position.x, self.position.y, child_asteroid_radius)
        first_child.velocity = first_child_velocity * 1.2
        second_child.velocity = second_child_velocity * 1.2

        # Return 5 if it is a medium asteroid
        if self.radius == ASTEROID_MIN_RADIUS * 2:
            return 5

        # Return 10 if it is a large asteroid
        return 10
