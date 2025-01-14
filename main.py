import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    # restrict our game for 60 fps
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2

        player = Player(x, y)
        player.draw(screen)

        # flip updates the full display surface to the screen
        pygame.display.flip()
        # updates the clock and convert from ms to seconds
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
