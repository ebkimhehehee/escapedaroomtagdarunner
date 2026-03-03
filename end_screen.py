import pygame


class End_screen:

    def __init__(self, screen: pygame.Surface, reddie_score: int, blu_score: int):
        self.screen = screen
        self.smth = "smth"
        self.reddie_score = reddie_score
        self.blu_score = blu_score
        if self.reddie_score == self.blu_score:
            self.winner = "YOU TIED (boring)"
            self.winnercolor = "#ffffff"
        elif self.reddie_score > self.blu_score:
            self.winner = "REDDIE WINS"
            self.winnercolor = "#ff0000"
        else: 
            self.winner = "BLU WINS"
            self.winnercolor = "#0026ff"
        self.bye = "Catch you next time!"
        self.reddie = pygame.transform.scale(pygame.image.load("assets/red.png").convert_alpha(), (200,200))
        self.blu = pygame.transform.scale(pygame.image.load("assets/blue.png").convert_alpha(), (200,200))
        self.fontscores = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 40)
        self.fontwinner = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 80)
        self.fontbye = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 50)

    def update(self):

        
        reddie_score_image = self.fontscores.render(f"REDDIE: {self.reddie_score}", True, "#ff0000")
        blu_score_image = self.fontscores.render(f"BLU: {self.blu_score}", True, "#0026ff")
        winner_image = self.fontwinner.render(self.winner, True, self.winnercolor)
        bye_image = self.fontbye.render(f"Catch you next time!", True, "#ffffff")


        self.screen.blit(self.reddie, (1100, 200))
        self.screen.blit(self.blu, (50, 500))

        self.screen.blit(reddie_score_image, (400, 30))
        self.screen.blit(blu_score_image, (850, 30))
        self.screen.blit(winner_image, (450, 300))
        self.screen.blit(bye_image, (500, 600))





def init_end_screen(screen: pygame.Surface, reddie_score: int, blu_score: int):
    return End_screen(screen, reddie_score, blu_score)