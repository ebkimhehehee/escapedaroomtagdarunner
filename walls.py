import pygame
from random import randrange




class Wall:


   def __init__(
       self, screen: pygame.Surface, x: int, y: int, width: int, height: int, color: str
   ) -> None:
       self.screen = screen
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.color = color


   def display(self):
       pygame.draw.rect(
           self.screen,
           self.color,
           (
               self.x - 0.5 * self.width,
               self.y - 0.5 * self.height,
               self.width,
               self.height,
           ),
       )


