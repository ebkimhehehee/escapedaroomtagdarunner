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
            7,
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
            7,
        )
        return p_one, p_two

    def update(self, screen: pygame.Surface, runner: Player, tagger: Player) -> bool:
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
            runner.speed = 7
            tagger.speed = 7
        if score_tagger:
            if tagger.color == self.p1.color:
                self.p1_score += 1
            if tagger.color == self.p2.color:
                self.p2_score += 1
            runner.speed = 7
            tagger.speed = 7

        right_score_image = self.font.render(
            f"BLU: {self.p2_score}", True, self.p2.color
        )
        left_score_image = self.font.render(
            f"REDDIE: {self.p1_score}", True, self.p1.color
        )


        screen.blit(
            left_score_image, (0.2 * screen.get_width(), 0.02 * screen.get_height())
        )
        screen.blit(
            right_score_image, (0.7 * screen.get_width(), 0.02 * screen.get_height())
        )
        return score_runner


def init_l1(screen: pygame.Surface, wall_color: str):
    walls = [
        Wall(screen, 100, 30, 300, 100, wall_color),
        Wall(screen, 600, 200, 50, 300, wall_color),
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
    orbs = [Orb(screen) for _ in range(11)]
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
        Wall(
            screen,
            50,
            500,
            120,
            20,
            wall_color,
        ),
        Wall(
            screen,
            50,
            500,
            120,
            20,
            wall_color,
        ),
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
    orbs = [Orb(screen) for _ in range(11)]
    return Level(screen, "#79CAFF", (750, 335), (25, 535), (1180, 170), walls, orbs)


def init_l3(screen: pygame.Surface, wall_color: str):  # esther #x,y, width, length
    walls = [
        Wall(screen, 100, 0, 60, 500, wall_color),
        Wall(screen, 0, 400, 1600, 60, wall_color),
        Wall(screen, 250, 240, 60, 300, wall_color),
        Wall(screen, 400, 0, 60, 500, wall_color),
        Wall(screen, 550, 240, 60, 300, wall_color),
        Wall(screen, 700, 0, 60, 500, wall_color),
        Wall(screen, 980, 0, 90, 1400, wall_color),
        Wall(screen, 1200, 500, 80, 600, wall_color),
        Wall(screen, 250, 850, 60, 600, wall_color),
        Wall(screen, 600, 850, 60, 600, wall_color),
        Wall(screen, 420, 520, 60, 300, wall_color),
        Wall(screen, 800, 520, 60, 300, wall_color),
        Wall(screen, 1200, 250, 200, 60, wall_color),
        Wall(screen, 1300, 100, 100, 100, wall_color),
    ]
    orbs = [Orb(screen) for _ in range(11)]
    return Level(screen, "#c62820", (0, 0), (1000, 700), (500, 700), walls, orbs)
# player one reddie, player 2 blu, end point


def init_l4(screen: pygame.Surface, wall_color: str):  # Esther - clean circular maze
    walls = [
        Wall(screen, 550, 200, 600, 30, wall_color), 
        Wall(screen, 110, 0, 30, 1200, wall_color),  
        Wall(screen, 250, 600, 30, 600, wall_color),
        Wall(screen, 1200, 600, 30, 600, wall_color), 
        Wall(screen, 970, 300, 30, 900, wall_color), 
        Wall(screen, 630, 82, 670, 30, wall_color), 
        Wall(screen, 600, 600, 520, 30, wall_color), 
        Wall(screen, 860, 400, 30, 420, wall_color), 
        Wall(screen, 350, 270, 20, 150, wall_color), 
        Wall(screen, 350, 550, 20, 100, wall_color), 
        Wall(screen, 450, 390, 20, 250, wall_color),
        Wall(screen, 600, 270, 320, 20, wall_color),
        Wall(screen, 600, 520, 320, 20, wall_color),
        Wall(screen, 750, 350, 20, 150, wall_color), 
        Wall(screen, 550, 700, 600, 20, wall_color), 
        Wall(screen, 1200, 300, 250, 20, wall_color), 
        Wall(screen, 1200, 0, 30, 400, wall_color), 
        Wall(screen, 1350, 600, 100, 20, wall_color), 
        Wall(screen, 1260, 700, 120, 20, wall_color), 
    ]

    orbs = [Orb(screen) for _ in range(11)]

    return Level(
        screen,
        "#cfeaff",
        (50, 50),     
        (700, 400), 
        (1350, 750),    
        walls,
        orbs,
    )


def init_l5(screen: pygame.Surface, wall_color: str):
    walls = [
        Wall(screen, 70, 700, 150, 200, wall_color),
        Wall(screen, 100, 590, 290, 35, wall_color),
        Wall(screen, 200, 790, 300, 50, wall_color),
        Wall(screen, 220, 690, 50, 50, wall_color),
        Wall(screen, 320, 720, 40, 110, wall_color),
        Wall(screen, 400, 780, 200, 100, wall_color),
        Wall(screen, 50, 525, 100, 100, wall_color),
        Wall(screen, 230, 500, 150, 50, wall_color),
        Wall(screen, 400, 540, 200, 130, wall_color),
        Wall(screen, 445, 640, 110, 70, wall_color),
        Wall(screen, 1000, 280, 80, 220, wall_color),
        Wall(screen, 1090, 340, 150, 100, wall_color),
        Wall(screen, 1205, 315, 80, 150, wall_color),
        Wall(screen, 1110, 80, 300, 50, wall_color),
        Wall(screen, 1105, 150, 30, 150, wall_color),
        Wall(screen, 1230, 115, 220, 120, wall_color),
        Wall(screen, 1330, 223, 50, 335, wall_color),
        Wall(screen, 730, 400, 150, 300, wall_color),
        Wall(screen, 50, 50, 190, 150, wall_color),
        Wall(screen, 250, 330, 250, 50, wall_color),
        Wall(screen, 350, 100, 250, 50, wall_color),
        Wall(screen, 100, 280, 50, 150, wall_color),
        Wall(screen, 500, 150, 50, 150, wall_color),
        Wall(screen, 170, 215, 100, 20, wall_color),
        Wall(screen, 320, 280, 20, 100, wall_color),
        Wall(screen, 450, 215, 100, 20, wall_color),
        Wall(screen, 235, 130, 20, 50, wall_color),
        Wall(screen, 515, 300, 20, 200, wall_color),
        Wall(screen, 400, 315, 80, 20, wall_color),
        Wall(screen, 485, 400, 80, 20, wall_color),
        Wall(screen, 0, 155, 50, 100, wall_color),
        Wall(screen, 80, 345, 80, 20, wall_color),
        Wall(screen, 805, 675, 300, 80, wall_color),
        Wall(screen, 1100, 500, 290, 30, wall_color),
        Wall(screen, 1390, 690, 160, 400, wall_color),
        Wall(screen, 970, 400, 20, 50, wall_color),
        Wall(screen, 1235, 400, 20, 50, wall_color),
        Wall(screen, 1100, 400, 20, 50, wall_color),
        Wall(screen, 1170, 470, 20, 50, wall_color),
        Wall(screen, 1040, 470, 20, 50, wall_color),
        Wall(screen, 1320, 480, 20, 70, wall_color),
        Wall(screen, 1150, 570, 20, 140, wall_color),
        Wall(screen, 1150, 720, 200, 20, wall_color),
        Wall(screen, 1280, 600, 100, 20, wall_color),
        Wall(screen, 1240, 700, 20, 60, wall_color),
        Wall(screen, 1050, 700, 20, 60, wall_color),
        Wall(screen, 920, 415, 80, 20, wall_color),
        Wall(screen, 840, 335, 80, 20, wall_color),
        Wall(screen, 920, 260, 80, 20, wall_color),
        Wall(screen, 550, 260, 80, 20, wall_color),
        Wall(screen, 630, 330, 80, 20, wall_color),
        Wall(screen, 550, 400, 80, 20, wall_color),
        Wall(screen, 520, 485, 60, 20, wall_color),
        Wall(screen, 640, 540, 60, 20, wall_color),
        Wall(screen, 520, 640, 80, 20, wall_color),
        Wall(screen, 740, 90, 250, 120, wall_color),
        Wall(screen, 945, 610, 20, 60, wall_color),
        Wall(screen, 945, 720, 20, 60, wall_color),
        Wall(screen, 665, 790, 20, 60, wall_color),
        Wall(screen, 750, 790, 150, 20, wall_color),
    ]
    orbs = [Orb(screen) for _ in range(11)]
    return Level(screen, "#FFA3EB", (1280, 200), (150, 280), (170, 740), walls, orbs)


def init_l6(screen: pygame.Surface, wall_color: str):
    walls = [
        Wall(screen, 530, 400, 30, 250, wall_color),
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
    orbs = [Orb(screen) for _ in range(11)]
    return Level(screen, "#13004E", (1370, 550), (700, 400), (975, 25), walls, orbs)
