import pygame
import random


class Orb:

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.x = random.uniform(0, screen.get_width())
        self.y = random.uniform(0, screen.get_height())
        self.vx = random.uniform(-10, 10)
        self.vy = random.uniform(-10, 20)
        self.radi = random.uniform(10, 15)
        self.color = random.choice([(255, 0, 0), (0, 0, 255)])

    def display(self) -> None:
        pygame.draw.circle(
            self.screen, self.color, (int(self.x), int(self.y)), int(self.radi)
        )
