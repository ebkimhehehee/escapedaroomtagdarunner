import pygame


from player import Player
from walls import Wall
from startpoint import Start
from endpoint import End
from orbs import Orb
from tagging import tagged


class Level:
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(
        self,
        screen: pygame.Surface,
        screen_color: str,
        start1: tuple[int, int],
        start2: tuple[int, int],
        endpt: tuple[int, int],
        walls: list[Wall],
        orbs: list[Orb],
    ) -> None:
        self.screen = screen
        self.screen_color = screen_color
        self.start1, self.start2 = Start(screen, *start1, 50, 50), Start(
            screen, *start2, 50, 50
        )
        self.end = End(screen, *endpt, 50, 50)
        self.walls = walls
        self.orbs = orbs
        self.font = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 40)
        self.p1, self.p2 = self.init_players()
        self.p1_score = 0
        self.p2_score = 0
        self.effects = []

    def init_players(self) -> tuple[Player, Player]:
        p_one = Player(
            self.screen,
            self.start1.x,
            self.start1.y,
            pygame.K_w,
            pygame.K_s,
            pygame.K_a,
            pygame.K_d,
            (255, 0, 0),
            self,
            7.5,
        )
        p_two = Player(
            self.screen,
            self.start2.x,
            self.start2.y,
            pygame.K_UP,
            pygame.K_DOWN,
            pygame.K_LEFT,
            pygame.K_RIGHT,
            (0, 0, 255),
            self,
            7.5,
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
        if score_runner:
            if runner.color == self.p1.color:
                self.p1_score += 1
            if runner.color == self.p2.color:
                self.p2_score += 1
            runner.speed = 7.5
            tagger.speed = 7.5
        if score_tagger:
            if tagger.color == self.p1.color:
                self.p1_score += 1
            if tagger.color == self.p2.color:
                self.p2_score += 1
            runner.speed = 7.5
            tagger.speed = 7.5

        right_score_image = self.font.render(f"BLU: {self.p2_score}", True, self.p2.color)
        left_score_image = self.font.render(f"REDDIE: {self.p1_score}", True, self.p1.color)
        screen.blit(
            left_score_image, (0.2 * screen.get_width(), 0.02 * screen.get_height())
        )
        screen.blit(
            right_score_image, (0.7 * screen.get_width(), 0.02 * screen.get_height())
        )


def init_l1(screen: pygame.Surface, wall_color: str):
    walls = [
        Wall(screen, 100, 30, 300, 100, wall_color),
        Wall(screen, 600, 200, 50, 300, wall_color), 
        Wall(screen, 100, 800, 50, 500, wall_color),
        Wall(screen, 1000, 50, 300, 800, wall_color),
        Wall(screen, 1200, 700, 400, 200, wall_color),
        Wall(screen, 600, 600, 400, 200, wall_color),
        Wall(screen, 300, 300, 200, 300, wall_color),
        Wall(screen, 1200, 400, 200, 30, wall_color),
        Wall(screen, 1350, 200, 150, 30, wall_color),
        Wall(screen, 700, 450, 20, 100, wall_color),
        Wall(screen, 225, 650, 30, 150, wall_color),
        Wall(screen, 260, 630, 100, 20, wall_color),
        Wall(screen, 600, 700, 20, 100, wall_color),
        Wall(screen, 800, 800, 20, 100, wall_color),
        Wall(screen, 1190, 40, 80, 80, wall_color),
        Wall(screen, 800, 200, 100, 100, wall_color),
    ]
    orbs = [Orb(screen) for i in range(11)]
    return Level(screen, "#000000", (25, 100), (25, 775), (1350, 100), walls, orbs)


def init_l2(screen: pygame.Surface, wall_color: str):
    walls = [
        Wall(screen, 250, 350, 80, 500, wall_color),
        Wall(screen, 700, 250, 50, 250, wall_color),
        Wall(screen, 575, 350, 250, 50, wall_color),
        Wall(screen, 1150, 100, 400, 100, wall_color),
        Wall(screen, 1275, 200, 150, 100, wall_color),
        Wall(screen, 1325, 300, 50, 200, wall_color),
        Wall(screen, 1035, 310, 170, 170, wall_color),
        Wall(screen, 1160, 350, 150, 90, wall_color),
        Wall(screen, 700, 600, 50, 250, wall_color),
        Wall(screen, 200, 760, 500, 80, wall_color),
        Wall(screen, 50, 100, 100, 20, wall_color),
        Wall(screen, 170, 300, 100, 20, wall_color),
        Wall(screen, 50, 500, 120, 20, wall_color,),
        Wall(screen, 800, 300, 150, 20, wall_color),
        Wall(screen, 475, 100, 50, 250, wall_color),
        Wall(screen, 300, 180, 120, 20, wall_color),
        Wall(screen, 540, 550, 270, 20, wall_color),
        Wall(screen, 440, 690, 20, 70, wall_color),
        Wall(screen, 1300, 700, 200, 200, wall_color),
        Wall(screen, 850, 715, 270, 20, wall_color),
        Wall(screen, 1050, 610, 350, 20, wall_color),
        Wall(screen, 1020, 550, 20, 100, wall_color),
        Wall(screen, 1170, 400, 20, 170, wall_color),
    ]
    orbs = [Orb(screen) for i in range(11)]
    return Level(screen, "#79CAFF", (750, 335), (25, 535), (1180, 170), walls, orbs)


def init_l3(screen: pygame.Surface, wall_color: str):
    walls = []
    orbs = [Orb(screen) for i in range(11)]
    return Level(screen, "#5c2c0e",(0,0), (1200, 700), (500, 400), walls, orbs)

def init_l4(screen: pygame.Surface, wall_color: str):
    walls = []
    orbs = [Orb(screen) for i in range(11)]
    return Level(screen, "#ffffff",(0,0), (1200, 700), (500, 400), walls, orbs)

def init_l5(screen: pygame.Surface, wall_color: str):
    walls = [Wall(screen, 530, 400, 30, 250, wall_color),
             Wall(screen, 870, 400, 30, 250, wall_color),
             Wall(screen, 700, 290, 350, 30, wall_color),
             Wall(screen, 550, 510, 50, 30, wall_color),
             Wall(screen, 760, 510, 200, 30, wall_color),
             Wall(screen, 1200, 50, 400, 150, wall_color),
             Wall(screen, 200, 400, 150, 400, wall_color),
             Wall(screen, 1150, 450, 200, 50, wall_color),
             Wall(screen, 1225, 320, 50, 250, wall_color),
             Wall(screen, 1030, 550, 50, 250, wall_color),
             Wall(screen, 1300, 700, 200, 200, wall_color),
             Wall(screen, 250, 30, 500, 70, wall_color),
             Wall(screen, 650, 670, 500, 50, wall_color),
             Wall(screen, 300, 210, 120, 20, wall_color),
             Wall(screen, 440, 285, 150, 20, wall_color),
             Wall(screen, 440, 255, 20, 50, wall_color),
             Wall(screen, 350, 380, 150, 20, wall_color),
             Wall(screen, 500, 380, 30, 20, wall_color),
             Wall(screen, 450, 490, 180, 20, wall_color),
             Wall(screen, 360, 530, 20, 100, wall_color),
             Wall(screen, 360, 400, 20, 50, wall_color),
             Wall(screen, 450, 610, 20, 80, wall_color),
             Wall(screen, 1280, 465, 80, 20, wall_color),
             Wall(screen, 1180, 610, 100, 20, wall_color),
             Wall(screen, 1280, 205, 80, 20, wall_color),
             Wall(screen, 1360, 350, 90, 20, wall_color),
             Wall(screen, 1315, 320, 20, 80, wall_color),
             Wall(screen, 1010, 200, 20, 150, wall_color),
             Wall(screen, 1015, 400, 20, 70, wall_color),
             Wall(screen, 1060, 205, 110, 20, wall_color),
             Wall(screen, 1125, 275, 20, 160, wall_color),
             Wall(screen, 1110, 365, 50, 20, wall_color),
             Wall(screen, 410, 720, 20, 70, wall_color),
             Wall(screen, 890, 720, 20, 70, wall_color),
             Wall(screen, 650, 790, 20, 70, wall_color),
             Wall(screen, 900, 515, 70, 20, wall_color),
             Wall(screen, 980, 375, 50, 20, wall_color),
             Wall(screen, 900, 285, 70, 20, wall_color),
             Wall(screen, 670, 550, 20, 80, wall_color),
             Wall(screen, 740, 590, 160, 20, wall_color),
             Wall(screen, 890, 620, 20, 70, wall_color),
             Wall(screen, 360, 655, 80, 20, wall_color),
             Wall(screen, 135, 630, 20, 70, wall_color),
             Wall(screen, 135, 770, 20, 80, wall_color),
             Wall(screen, 135, 200, 20, 90, wall_color),
             Wall(screen, 500, 50, 20, 200, wall_color),
             Wall(screen, 680, 150, 380, 20, wall_color),
             ]
    orbs = [Orb(screen) for i in range(11)]
    return Level(screen, "#000000", (700,400), (1370,550), (975,25), walls, orbs)