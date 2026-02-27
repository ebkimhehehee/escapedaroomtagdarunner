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

        right_score_image = self.font.render(f"{self.p1_score}", True, self.p1.color)
        left_score_image = self.font.render(f"{self.p2_score}", True, self.p2.color)
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


def init_l2(screen: pygame.Surface):
    walls = [
        Wall(screen, 250, 350, 80, 500),
        Wall(screen, 700, 250, 50, 250),
        Wall(screen, 575, 350, 250, 50),
        Wall(screen, 1150, 100, 400, 100),
        Wall(screen, 1275, 200, 150, 100),
        Wall(screen, 1325, 300, 50, 200),
        Wall(screen, 1035, 310, 170, 170),
        Wall(screen, 1160, 350, 150, 90),
        Wall(screen, 700, 600, 50, 250),
        Wall(screen, 200, 760, 500, 80),
        Wall(screen, 50, 100, 100, 20),
        Wall(screen, 170, 300, 100, 20),
        Wall(screen, 50, 500, 120, 20),
        Wall(screen, 800, 300, 150, 20),
        Wall(screen, 475, 100, 50, 250),
        Wall(screen, 300, 180, 120, 20),
        Wall(screen, 540, 550, 270, 20),
        Wall(screen, 440, 690, 20, 70),
        Wall(screen, 1300, 700, 200, 200),
        Wall(screen, 850, 715, 270, 20),
        Wall(screen, 1050, 610, 350, 20),
        Wall(screen, 1020, 550, 20, 100),
        Wall(screen, 1170, 400, 20, 170)
    ]

    orbs = [Orb(screen) for i in range(10)]

    return Level(screen, "#000000", (750, 335), (25, 535), (1180, 170), walls, orbs)

