import pygame


class Start_screen:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.titlep1 = "ESCAPE DA ROOM"
        self.titlep2 = "TAG DA RUNNER"
        self.play = "press space to start"
        self.runner = "Hey runner! Navigate through the maze and escape da room by reaching the pink portal. But avoid the tagger at all costs, because if they catch you, you'll have to start all over again."
        self.tagger = "Hi tagger! Your job is to tag da runner. Don't let them reach the pink portal!"
        self.points = "RUNNER SCORES BY REACHING THE PINK PORTAL, TAGGER SCORES BY TAGGING DA RUNNER"
        self.run_tag = "Reddie starts as runner and Blu starts as tagger, but dont worry! These roles switch every level, so you're able to play as both runner and tagger. "
        self.orbs = "If the orb color matches you, it gives you a speed boost! Orbs with the opposite color slow you down... Be smart about how you use them :) They are both friend and foe"
        self.walls = "AND DON'T TOUCH THE WALLS, THEY AREN'T FRIENDLY"
        
        self.fonttitle = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 80)
        self.fontrules = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 30)
        self.fontplay = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 40)
        self.fontnames = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 30)
        
        self.reddie = pygame.transform.scale(pygame.image.load("assets/red.png").convert_alpha(), (100,100))
        self.blu = pygame.transform.scale(pygame.image.load("assets/blue.png").convert_alpha(), (100,100))
        self.names_y = 20
        self.reddie_name = "REDDIE" 
        self.reddie_x = 30
        self.blu_name= "BLU"
        self.blu_x = 1260
    

    def update(self):
        self.screen.fill("#000000")

        self.screen.blit(self.reddie, (self.reddie_x, self.names_y))
        self.screen.blit(self.blu, (self.blu_x, self.names_y))

        reddie_name_image = self.fontnames.render(f"{self.reddie_name}", True, "#ff0000")
        blu_name_image = self.fontnames.render(f"{self.blu_name}", True, "#0026ff")

        self.screen.blit(
            reddie_name_image, (self.reddie_x, self.names_y + 105)
        )
        self.screen.blit(
            blu_name_image, (self.blu_x, self.names_y + 105)
        )


        titlep1_image = self.fonttitle.render(f"{self.titlep1}", True, "#ff0000")
        titlep2_image = self.fonttitle.render(f"{self.titlep2}", True, "#0026ff")
        play_image =  self.fontplay.render(f"{self.play}", True, "#ffffff")
        runner_image = self.fontrules.render(f"{self.runner}", True, "#ffffff")
        tagger_image = self.fontrules.render(f"{self.tagger}", True, "#ffffff")
        points_image = self.fontrules.render(f"{self.points}", True, "#ffffff")
        run_tag_image = self.fontrules.render(f"{self.run_tag}", True, "#ffffff")
        orbs_image = self.fontrules.render(f"{self.orbs}", True, "#ffffff")
        walls_image = self.fontrules.render(f"{self.walls}", True, "#ffffff")







        self.screen.blit(
            titlep1_image, (0.33 * self.screen.get_width(), 0.05 * self.screen.get_height())
        )
        self.screen.blit(
            titlep2_image, (0.35 * self.screen.get_width(), 0.12 * self.screen.get_height())
        )
        self.screen.blit(
            play_image, (0.42 * self.screen.get_width(), 0.9 * self.screen.get_height())
        )


        self.screen.blit(
            runner_image, (0.05 * self.screen.get_width(), 0.2 * self.screen.get_height())
        )
        self.screen.blit(
            tagger_image, (0.05 * self.screen.get_width(), 0.3 * self.screen.get_height())
        )
        self.screen.blit(
            points_image, (0.05 * self.screen.get_width(), 0.4 * self.screen.get_height())
        )
        self.screen.blit(
            run_tag_image, (0.05 * self.screen.get_width(), 0.5 * self.screen.get_height())
        )
        self.screen.blit(
            orbs_image, (0.05 * self.screen.get_width(), 0.6 * self.screen.get_height())
        )
        self.screen.blit(
            walls_image, (0.05 * self.screen.get_width(), 0.7 * self.screen.get_height())
        )

def init_start_screen(screen: pygame.Surface):
    return Start_screen(screen)
