import pygame
from circleshape import CircleShape
from constants import *
import random

# asteroid.py

import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Initialize position, velocity, radius in the parent
        super().__init__(x, y, radius)

        # (No more self.x/self.y needed—CircleShape already set self.position)

    def draw(self, screen):
        # Draw from the up-to-date position vector
        pygame.draw.circle(
            screen,
            (150, 150, 150),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self, dt):
        # Move the position by the velocity vector
        self.position += self.velocity * dt


    def split(self):
        """
        Split this asteroid into two smaller ones upon destruction.
        """
        # Remove the current asteroid
        self.kill()

        # If it's already the smallest size, do nothing further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Determine split angle between 20 and 50 degrees
        split_angle = random.uniform(20, 50)

        # Original velocity vector
        orig_vel = self.velocity

        # Create two new velocity vectors, rotated in opposite directions and sped up
        vel1 = orig_vel.rotate(split_angle) * 1.2
        vel2 = orig_vel.rotate(-split_angle) * 1.2

        # New radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids at current position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vel2


