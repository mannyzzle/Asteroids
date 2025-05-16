# circleshape.py

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # auto-add into any sprite.Groups in self.containers
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius   = radius

    def draw(self, screen):
        # sub-classes override
        pass

    def update(self, dt):
        # sub-classes override
        pass

    def collides_with(self, other: "CircleShape") -> bool:
        """Return True if this circle overlaps the other."""
        dist = self.position.distance_to(other.position)
        return dist <= (self.radius + other.radius)
