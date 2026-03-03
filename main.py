import sys


import pygame
import pygame.locals


from levels import init_l1, init_l2, init_l3, init_l4, init_l5
from start_screen import init_start_screen
from end_screen import init_end_screen


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1400, 800))

    start_screen = init_start_screen(screen)
    level1 = init_l1(screen, "#565656")
    level2 = init_l2(screen, "#00c521")
    level3 = init_l3(screen, "#ff0000")
    level4 = init_l4(screen, "#FFFFFF")
    level5 = init_l5(screen, "#510CAC")



    end_screen = init_end_screen(
        screen, level2.p1_score, level2.p2_score
    )  # CHANGE TO LAST LEVEL
    state = "l5"

    while True:

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            if state == "startscreen":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = "l1"

        if state == "startscreen":
            start_screen.update()

        if state == "l1":
            level1.update(screen, level1.p1, level1.p2)

        if state == "l2":
            level2.update(screen, level2.p2, level2.p1)

        if state == "l3":
            level3.update(screen, level3.p1, level3.p2)

        if state == "l4":
            level4.update(screen, level4.p2, level4.p1)

        if state == "l5":
            level5.update(screen, level5.p1, level5.p2)

        if state == "endscreen":
            end_screen.update()

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
