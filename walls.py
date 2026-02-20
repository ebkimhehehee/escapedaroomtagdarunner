import pygame
from random import randrange




class Wall:


   def __init__(self, screen: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
       self.screen = screen
       self.x = x
       self.y = y
       self.width = width
       self.height = height


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



