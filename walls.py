import pygame
from random import randrange




class Wall:


   def __init__(self, screen: pygame.Surface) -> None:
       self.screen = screen
       self.x = randrange(0, screen.get_width())
       self.y = randrange(0, screen.get_height())
       self.width = 50
       self.height = 50


   def display(self):
       pygame.draw.rect(
           self.screen,
           "#5C5C5C",
           (
               self.x - 0.5 * self.width,
               self.y - 0.5 * self.height,
               self.width,
               self.height,
           ),
       )



