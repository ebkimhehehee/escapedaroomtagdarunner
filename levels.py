import pygame

from player import Player
from walls import Wall
from startpoint import Start
from endpoint import End
from orbs import Orb
from tagging import tagged

class Level:

    def __init__(
        self,
        screen: pygame.Surface,
        screen_color: str,
        start1: tuple[int, int],
        start2: tuple[int, int],
        endpt: tuple[int, int],
        walls: list[Wall],
        orbs: list[Orb]
    ) -> None:
        self.screen = screen
        self.screen_color = screen_color
        self.start1, self.start2 = Start(screen, *start1, 50, 50), Start(screen, *start2, 50, 50)
        self.end = End(screen, *endpt, 50, 50)
        self.walls = walls
        self.orbs = orbs
        self.font = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 40)
        self.p1, self.p2 = self.init_players()
        self.p1_score = 0
        self.p2_score = 0

    def init_players(self) -> tuple[Player, Player]:
        p_one = Player(
            self.screen,
            self.start1.x,
            self.start1.y,
            pygame.K_w,
            pygame.K_s,
            pygame.K_a,
            pygame.K_d,
            "#FF0000",
            self
        )
        p_two = Player(
            self.screen,
            self.start2.x,
            self.start2.y,
            pygame.K_UP,
            pygame.K_DOWN,
            pygame.K_LEFT,
            pygame.K_RIGHT,
            "#0026FF",
            self
        )
        return p_one, p_two

    def update(self, screen: pygame.Surface, runner: Player, tagger: Player) -> None:
        screen.fill(self.screen_color)
        for orb in self.orbs:
            orb.display()

        self.start1.display()
        self.start2.display()
        self.end.display()

        for w in self.walls:
            w.display()
        for wall in self.walls:
            self.p1.runinto(wall)
        for wall in self.walls:
            self.p2.runinto(wall)

        self.p1.update()
        self.p1.display()
        self.p2.update()
        self.p2.display()


        score_runner = runner.reachend(self.end)
        score_tagger = tagged(runner, tagger)
        if runner.color == "#ff0000":
            if score_runner:
                self.p1_score += 1
            if score_tagger:
                self.p2_score += 1
        if runner.color == "#0026ff":
            if score_runner:
                self.p2_score += 1
            if score_tagger:
                self.p1_score += 1
        
        right_score_image = self.font.render(f"{self.p1_score}", True, "#ff0000")
        left_score_image = self.font.render(f"{self.p2_score}", True, "#0026ff")
        screen.blit(
            left_score_image, (0.2 * screen.get_width(), 0.1 * screen.get_height())
        )
        screen.blit(
            right_score_image, (0.8 * screen.get_width(), 0.1 * screen.get_height())
        )


def init_l1(screen: pygame.Surface):
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
        Wall(screen, 800, 200, 100, 100),
    ]
    orbs = [Orb(screen) for i in range(10)]

    return Level(screen, "#000000", (25, 100), (25, 775), (1350, 100), walls, orbs)

