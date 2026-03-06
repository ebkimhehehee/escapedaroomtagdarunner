import pygame


import pygame
yaysound = None
from walls import Wall
from endpoint import End
from orbs import Orb


RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Player:


   def __init__(
       self,
       screen: pygame.Surface,
       x: float,
       y: float,
       key_up: int,
       key_down: int,
       key_left: int,
       key_right: int,
       color: tuple[int, int, int],
       level: "Level", # type: ignore
       speed: float
   ) -> None:
       self.screen = screen
       self.x, self.y = x, y
       self.width, self.height = 30, 30
       self.vx = 0
       self.vy = 0
       self.up = key_up
       self.down = key_down
       self.left = key_left
       self.right = key_right
       self.color = color
       self.init_x = x
       self.init_y = y
       self.level = level
       self.speed = 7
       self.trail = []


       if self.color == (255, 0, 0):
           self.face = pygame.image.load("assets/red.png").convert_alpha()
       else:
           self.face = pygame.image.load("assets/blue.png").convert_alpha()
      
       self.face = pygame.transform.scale(self.face, (self.width, self.height))


   def runinto(self, wall: Wall) -> None:
       left_edge = wall.x - wall.width / 2 - self.width * (1 / 2)
       right_edge = wall.x + wall.width / 2 + self.width * (1 / 2)
       top_edge = wall.y - wall.height / 2 - self.width * (1 / 2)
       bottom_edge = wall.y + wall.height / 2 + self.width * (1 / 2)
       if left_edge < self.x < right_edge and top_edge < self.y < bottom_edge:
           self.x = self.init_x
           self.y = self.init_y


   def reachend(self, endpt: End) -> bool:
    global yaysound

    if yaysound is None:
        yaysound = pygame.mixer.Sound("yay.wav")
    left_edge = endpt.x - endpt.width / 2 - self.width * (1 / 2)
    right_edge = endpt.x + endpt.width / 2 + self.width * (1 / 2)
    top_edge = endpt.y - endpt.height / 2 - self.width * (1 / 2)
    bottom_edge = endpt.y + endpt.height / 2 + self.width * (1 / 2)

    if left_edge < self.x < right_edge and top_edge < self.y < bottom_edge:
            if not pygame.mixer.get_busy():
                yaysound.play()
            self.x = self.init_x
            self.y = self.init_y
            return True 
    return False
  






   def touch_orb(self, orb: Orb) -> bool:
       x_diff = abs(self.x - orb.x)
       y_diff = abs(self.y - orb.y)


       if x_diff < self.width / 2 + orb.radi and y_diff <self.height / 2 +orb.radi:
           if self.color == orb.color:
               self.speed *= 1.3
               self.speed *= 1.3
           else:
               self.speed *= 0.7
               self.speed *= 0.7
           return True
       return False




   def update(self) -> None:
       pushed = pygame.key.get_pressed()


       self.vx = pushed[self.left] * -self.speed + pushed[self.right] * self.speed
       self.vy = pushed[self.up] * -self.speed + pushed[self.down] * self.speed


       self.x += self.vx
       self.y += self.vy


       if self.x < 0.7 * self.width:
           self.x = 0.7 * self.width
       if self.x > self.screen.get_width() - 0.7 * self.width:
           self.x = self.screen.get_width() - 0.7 * self.width


       if self.y < 0.7 * self.height:
           self.y = 0.7 * self.height
       if self.y > self.screen.get_height() - 0.7 * self.height:
           self.y = self.screen.get_height() - 0.7 * self.height


       for orb in self.level.orbs:
           if self.touch_orb(orb):
               self.level.orbs.remove(orb)


       self.trail.append((self.x, self.y))


       if len(self.trail) > 4:
           self.trail.pop(0)

   def display(self) -> None:
       rect_x = self.x - self.width / 2
       rect_y = self.y - self.height / 2


       for pos in self.trail:
           pygame.draw.circle(
           self.screen,
           self.color,
           (int(pos[0]), int(pos[1])),
           4
       )


       self.screen.blit(self.face, (rect_x, rect_y))


      
