import sys


import pygame
import pygame.locals


from player import Player
from walls import Wall
from startpoint import Start
from orbs import Orb
from endpoint import End


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))

    state = "start"

    orbeez = [Orb(screen) for i in range(10)]

    start1 = Start(screen, 25, 100, 50, 50)
    start2 = Start(screen, 25, 775, 50, 50)
    endpt = End(screen, 1350, 100, 50, 50)
    font = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 40)

    spawn1 = start1
    spawn2 = start2

    p_one = Player(
        screen,
        spawn1.x,
        spawn1.y,
        pygame.K_w,
        pygame.K_s,
        pygame.K_a,
        pygame.K_d,
        "#FF0000",
    )
    left_score = 0

    p_two = Player(
        screen,
        spawn2.x,
        spawn2.y,
        pygame.K_UP,
        pygame.K_DOWN,
        pygame.K_LEFT,
        pygame.K_RIGHT,
        "#0026FF",
    )
    right_score = 0

    walls = [
        Wall(screen, 100, 30, 300, 100),
        Wall(screen, 600, 200, 50, 300),
        Wall(screen, 100, 800, 50, 500),
        Wall(screen, 1000, 50, 300, 800),
        Wall(screen, 1200, 700, 400, 200),
        Wall(screen, 600, 600, 400, 200),
        Wall(screen, 300, 300, 200, 300),
        Wall(screen, 1200, 400, 200, 30),
        Wall(screen, 1350, 200, 150, 30),
        Wall(screen, 700, 450, 20, 100),
        Wall(screen, 225, 650, 30, 150),
        Wall(screen, 260, 630, 100, 20),
        Wall(screen, 600, 700, 20, 100),
        Wall(screen, 800, 800, 20, 100),
        Wall(screen, 1190, 40, 80, 80),
        Wall(screen, 800, 200, 100, 100)
    ]

    while True:
        screen.fill("#000000")

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.locals.K_v:
                if event.key == pygame.K_SPACE:
                    if state == "start":
                        state = "game"
                    elif state == "gane":
                        state = "dead"
                if event.key == pygame.K_r:
                    if state == "dead":
                        state = "start"
        if state == "start":
            screen.fill("#000000")
        elif state == "game":
            screen.fill("#ffffff")
        elif state == "dead":
            screen.fill("#911B1B")

        start1.display()
        start2.display()
        endpt.display()

        for orb in orbeez:
            orb.display()

        p_one.update()
        p_one.display()
        p_two.update()
        p_two.display()

        for wall in walls:
            p_one.runinto(wall)
        for wall in walls:
            p_two.runinto(wall)
        for w in walls:
            w.display()

        p_one.reachend(endpt)

        scorer = ...
        if scorer == 1:
            right_score += 1
        elif scorer == 2:
            left_score += 1
        right_score_image = font.render(f"{right_score}", True, "#ffffff")
        left_score_image = font.render(f"{left_score}", True, "#ffffff")
        screen.blit(
            left_score_image, (0.2 * screen.get_width(), 0.1 * screen.get_height())
        )
        screen.blit(
            right_score_image, (0.8 * screen.get_width(), 0.1 * screen.get_height())
        )

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
