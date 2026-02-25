import pygame
import random

RED = (255, 0, 0)
BLUE = (0, 0, 255)
class Orb:

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.x = random.uniform(0, screen.get_width())
        self.y = random.uniform(0, screen.get_height())
        self.vx = random.uniform(-10, 10)
        self.vy = random.uniform(-10, 20)
        self.radi = random.uniform(10,15)
        self.color = random.choice([RED, BLUE])

    def display(self) -> None: 
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radi) 
    
