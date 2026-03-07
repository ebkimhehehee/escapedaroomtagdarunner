import pygame


class Start_screen:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.titlep1 = "ESCAPE DA ROOM"
        self.titlep2 = "TAG DA RUNNER"
        self.play = "press space to start"

        self.runner1 = "Hey runner! Escape da room"
        self.runner2 = "by reaching the pink portal."
        self.runner3 = "But avoid the tagger at all costs!"

        self.tagger1 = "Hi tagger! Your job is"
        self.tagger2 = "to tag da runner. Don't let"
        self.tagger3 = "them reach the pink portal!"

        self.points = "RUNNER SCORES BY REACHING THE PINK PORTAL,  TAGGER SCORES BY TAGGING DA RUNNER"

        self.run_tag1 = "Reddie starts as runner and Blu starts"
        self.run_tag2 = "as tagger, but dont worry! These roles switch"
        self.run_tag3 = "every level, so you can play as both."

        self.orbs1 = "If the orb color matches you, it gives"
        self.orbs2 = "you a speed boost! Orbs with the opposite"
        self.orbs3 = "color slow you down... Be smart about how"
        self.orbs4 = "you use them :) They are both friend and foe"

        self.walls = "AND DON'T TOUCH THE WALLS, THEY AREN'T FRIENDLY"

        self.fonttitle = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 90)
        self.fontrules = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 30)
        self.fontpoints = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 35)
        self.fontwalls = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 50)
        self.fontplay = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 40)
        self.fontnames = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 30)


        self.reddie = pygame.transform.scale(
            pygame.image.load("assets/red.png").convert_alpha(), (100, 100)
        )
        self.blu = pygame.transform.scale(
            pygame.image.load("assets/blue.png").convert_alpha(), (100, 100)
        )
        self.names_y = 20
        self.reddie_name = "REDDIE"
        self.reddie_x = 30
        self.blu_name = "BLU"
        self.blu_x = 1260

    def update(self):
        self.screen.fill("#000000")

        self.screen.blit(self.reddie, (self.reddie_x, self.names_y))
        self.screen.blit(self.blu, (self.blu_x, self.names_y))

        reddie_name_image = self.fontnames.render(
            f"{self.reddie_name}", True, "#ff0000"
        )
        blu_name_image = self.fontnames.render(f"{self.blu_name}", True, "#2646ff")

        self.screen.blit(reddie_name_image, (self.reddie_x, self.names_y + 105))
        self.screen.blit(blu_name_image, (self.blu_x, self.names_y + 105))

        titlep1_image = self.fonttitle.render(f"{self.titlep1}", True, "#ff0000")
        titlep2_image = self.fonttitle.render(f"{self.titlep2}", True, "#2646ff")
        play_image = self.fontplay.render(f"{self.play}", True, "#ffb1ee")
        runner1_image = self.fontrules.render(f"{self.runner1}", True, "#ffffff")
        runner2_image = self.fontrules.render(f"{self.runner2}", True, "#ffffff")
        runner3_image = self.fontrules.render(f"{self.runner3}", True, "#ffffff")
        tagger1_image = self.fontrules.render(f"{self.tagger1}", True, "#ffffff")
        tagger2_image = self.fontrules.render(f"{self.tagger2}", True, "#ffffff")
        tagger3_image = self.fontrules.render(f"{self.tagger3}", True, "#ffffff")
        points_image = self.fontpoints.render(f"{self.points}", True, "#ffffff")
        run_tag1_image = self.fontrules.render(f"{self.run_tag1}", True, "#ffffff")
        run_tag2_image = self.fontrules.render(f"{self.run_tag2}", True, "#ffffff")
        run_tag3_image = self.fontrules.render(f"{self.run_tag3}", True, "#ffffff")
        orbs1_image = self.fontrules.render(f"{self.orbs1}", True, "#ffffff")
        orbs2_image = self.fontrules.render(f"{self.orbs2}", True, "#ffffff")
        orbs3_image = self.fontrules.render(f"{self.orbs3}", True, "#ffffff")
        orbs4_image = self.fontrules.render(f"{self.orbs4}", True, "#ffffff")
        walls_image = self.fontwalls.render(f"{self.walls}", True, "#ffffff")

        self.screen.blit(
            titlep1_image,
            (self.screen.get_width()/2 - titlep1_image.get_width()/2, 0.05 * self.screen.get_height()),
        )
        self.screen.blit(
            titlep2_image,
            (self.screen.get_width()/2 - titlep2_image.get_width()/2, 0.13 * self.screen.get_height()),
        )
        self.screen.blit(
            play_image, (self.screen.get_width()/2 - play_image.get_width()/2, 0.9 * self.screen.get_height())
        )
        self.screen.blit(
            runner1_image,
            (0.2 * self.screen.get_width(), 0.25 * self.screen.get_height()),
        )
        self.screen.blit(
            runner2_image,
            (0.2 * self.screen.get_width(), 0.3 * self.screen.get_height()),
        )
        self.screen.blit(
            runner3_image,
            (0.2 * self.screen.get_width(), 0.35 * self.screen.get_height()),
        )
        self.screen.blit(
            tagger1_image,
            (0.58 * self.screen.get_width(), 0.25 * self.screen.get_height()),
        )
        self.screen.blit(
            tagger2_image,
            (0.58 * self.screen.get_width(), 0.3 * self.screen.get_height()),
        )
        self.screen.blit(
            tagger3_image,
            (0.58 * self.screen.get_width(), 0.35 * self.screen.get_height()),
        )
        self.screen.blit(
            points_image,
            (self.screen.get_width()/2 - points_image.get_width()/2, 0.45 * self.screen.get_height()),
        )
        self.screen.blit(
            run_tag1_image,
            (0.18 * self.screen.get_width(), 0.55 * self.screen.get_height()),
        )
        self.screen.blit(
            run_tag2_image,
            (0.18 * self.screen.get_width(), 0.6 * self.screen.get_height()),
        )
        self.screen.blit(
            run_tag3_image,
            (0.18 * self.screen.get_width(), 0.65 * self.screen.get_height()),
        )
        self.screen.blit(
            orbs1_image, (0.56 * self.screen.get_width(), 0.55 * self.screen.get_height())
        )
        self.screen.blit(
            orbs2_image, (0.56 * self.screen.get_width(), 0.6 * self.screen.get_height())
        )
        self.screen.blit(
            orbs3_image, (0.56 * self.screen.get_width(), 0.65 * self.screen.get_height())
        )
        self.screen.blit(
            orbs4_image, (0.56 * self.screen.get_width(), 0.7 * self.screen.get_height())
        )
        self.screen.blit(
            walls_image,
            (self.screen.get_width()/2 - walls_image.get_width()/2, 0.78 * self.screen.get_height()),
        )


def init_start_screen(screen: pygame.Surface):
    return Start_screen(screen)
