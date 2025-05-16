# player.py
import pygame
from circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right   = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, pygame.Color('white'), self.triangle(), 2)

    def rotate(self, dt: float):
        # dt is in seconds; turn speed is degrees/sec
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        # fire in facing direction
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.shoot_timer > 0:
            self.shoot_timer = max(0, self.shoot_timer - dt)
        if keys[pygame.K_a]:
            # rotate left (negative dt)
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # rotate right
            self.rotate(dt)
        # move forward/back
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        # shooting (only if timer has expired)
        if keys[pygame.K_SPACE] and self.shoot_timer == 0:
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        # point (0,1) in the ship’s “up” direction, rotated by its angle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt





