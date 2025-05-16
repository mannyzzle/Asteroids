# shot.py
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        # init position & radius
        super().__init__(x, y, SHOT_RADIUS)
        # we'll set velocity from the player
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 0),  # yellow shot
            (int(self.position.x), int(self.position.y)),
            self.radius
        )

    def update(self, dt):
        # move in straight line
        self.position += self.velocity * dt
        # kill it when off-screen here
