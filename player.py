from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "#fafafa", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Prevent player from shooting if shoot timer is greater than 0
        if self.shoot_timer > 0:
            return

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        # Decrease the shoot timer
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        # Rotate left
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        # Rotate right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        # Move up
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        # Move down
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)

        # Shoot
        if keys[pygame.K_SPACE]:
            self.shoot()
