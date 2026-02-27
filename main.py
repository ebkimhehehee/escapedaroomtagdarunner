import sys

import pygame
import pygame.locals

from levels import init_l1, init_l2


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))

    level1 = init_l1(screen)
    level2 = init_l2(screen)
    state = "l2"

    while True:

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        if state == "l1":
            level1.update(screen, level1.p1, level1.p2)
        if state == "l2":
            level2.update(screen, level2.p2, level2.p1)

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
