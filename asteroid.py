import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # pass radius into the parent initializer
        super().__init__(x, y, radius)

        # (optional) if CircleShape doesn’t already set these, you can keep them
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (150, 150, 150),
            (int(self.x), int(self.y)),
            self.radius,
            2
        )

    def update(self, dt):
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt
