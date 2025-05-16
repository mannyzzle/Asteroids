# MAIN.PY
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from shot import Shot
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
    font   = pygame.font.Font(None, 36)
    score = 0

    # --- Set up sprite groups ---
    asteroids = Group()
    updatable = Group()
    shots = Group()
    drawable = Group()

    # Tell our classes which groups to auto-add to
    Asteroid.containers      = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

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

        for ast in asteroids:
            if ast.collides_with(player):
                print(f"Game over! Final score: {score}")
                pygame.quit()
                sys.exit()
            for bull in shots:
                if bull.collides_with(ast):
                    r = ast.radius
                    ast.split()
                    bull.kill()
                    # award points by size
                    if r <= ASTEROID_MIN_RADIUS:
                        score += ASTEROID_SMALL_POINTS
                    elif r <= ASTEROID_MIN_RADIUS * 2:
                        score += ASTEROID_MEDIUM_POINTS
                    else:
                        score += ASTEROID_LARGE_POINTS


        # Draw
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
