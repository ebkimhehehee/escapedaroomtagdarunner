import sys


import pygame
import pygame.locals


from levels import init_l1, init_l2, init_l3, init_l4, init_l5, init_l6
from transition_levels import init_t1, init_t2, init_t3, init_t4, init_t5, init_t6
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
    level5 = init_l5(screen, "#F9E579")
    level6 = init_l6(screen, "#510CAC")
    trans1 = init_t1(screen, 1, level1.p1)
    trans2 = init_t2(screen, 2, level2.p2)
    trans3 = init_t3(screen, 3, level3.p1)
    trans4 = init_t4(screen, 4, level4.p2)
    trans5 = init_t5(screen, 5, level5.p1)
    trans6 = init_t6(screen, 6, level6.p2)
    end_screen = init_end_screen(screen)
    state = "l6"

    while True:

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            if state == "start_screen":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = "t1"

            elif state == "t1":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = "l1"

            elif state == "t2":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = "l2"

            elif state == "t3":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = "l3"

            elif state == "t4":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = "l4"

            elif state == "t5":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = "l5"
            
            elif state == "t6":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = "l6"

        if state == "start_screen":
            start_screen.update()

        elif state == "t1":
            trans1.update(level1.p1)

        elif state == "t2":
            trans2.update(level2.p2)

        elif state == "t3":
            trans3.update(level3.p1)

        elif state == "t4":
            trans4.update(level4.p2)

        elif state == "t5":
            trans5.update(level5.p1)
        
        elif state == "t6":
            trans6.update(level6.p2)

        elif state == "l1":
            score_runner = level1.update(screen, level1.p1, level1.p2)
            if score_runner:
                level2.p1_score = level1.p1_score
                level2.p2_score = level1.p2_score
                trans2.reddiescore = level1.p1_score
                trans2.bluscore = level1.p2_score
                state = "t2"

        elif state == "l2":
            score_runner = level2.update(screen, level2.p2, level2.p1)
            if score_runner:
                level3.p1_score = level2.p1_score
                level3.p2_score = level2.p2_score
                trans3.reddiescore = level2.p1_score
                trans3.bluscore = level2.p2_score
                state = "t3"

        elif state == "l3":
            score_runner = level3.update(screen, level3.p1, level3.p2)
            if score_runner:
                level4.p1_score = level3.p1_score
                level4.p2_score = level3.p2_score
                trans4.reddiescore = level3.p1_score
                trans4.bluscore = level3.p2_score
                state = "t4"

        elif state == "l4":
            score_runner = level4.update(screen, level4.p2, level4.p1)
            if score_runner:
                level5.p1_score = level4.p1_score
                level5.p2_score = level4.p2_score
                trans5.reddiescore = level4.p1_score
                trans5.bluscore = level4.p2_score
                state = "t5"

        elif state == "l5":
            score_runner = level5.update(screen, level5.p1, level5.p2)
            if score_runner:
                level6.p1_score = level5.p1_score
                level6.p2_score = level5.p2_score
                trans6.reddiescore = level5.p1_score
                trans6.bluscore = level5.p2_score
                state = "t6"
        
        elif state == "l6":
            score_runner = level6.update(screen, level6.p1, level6.p2)
            if score_runner:
                end_screen.reddie_score = level6.p1_score
                end_screen.blu_score = level6.p2_score
                state = "end_screen"

        elif state == "end_screen":
            end_screen.update()

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
