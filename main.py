# MAIN.PY
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from pygame.sprite import Group
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # --- Set up sprite groups ---
    asteroids = Group()
    updatable = Group()
    drawable = Group()

    # Tell our classes which groups to auto-add to
    Asteroid.containers      = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Create our game objects
    player         = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()  # automatically goes into `updatable`

    # Add the player
    updatable.add(player)
    drawable.add(player)

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update (and cap FPS + compute dt)
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        # Draw
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
