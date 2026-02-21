import random

import pygame

class Orb:

    def __init__(self, screen:pygame.Surface) -> None:
        self.screen = screen
        self.x = random.uniform(0, screen.get_width())
        self.y = random.uniform(0, screen.get_height())
        self.vx = random.uniform(-10,10)
        self.vy = random.uniform(-10, 20)
        self.radi = random.uniform(15,20)
        self.color = (random.randint(200,255), random.randint(0,255), random.randint(0,255))


    def display(self) -> None:#display displays the ball...
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radi) # type: ignore
def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
