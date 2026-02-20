import pygame


from walls import Wall

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
       color: str,
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

   def runinto(self, wall: Wall) -> None:
        left_edge = wall.x - wall.width / 2 - self.width*(1/2)
        right_edge = wall.x + wall.width / 2 + self.width*(1/2)
        top_edge = wall.y - wall.height / 2 - self.width*(1/2)
        bottom_edge = wall.y + wall.height / 2 + self.width*(1/2)
        if left_edge < self.x < right_edge and top_edge < self.y < bottom_edge:
            self.x == wall.x and self.y == wall.y


   def update(self) -> None:
       pushed = pygame.key.get_pressed()


       self.vx = pushed[self.left] * -5 + pushed[self.right] * 5
       self.vy = pushed[self.up] * -5 + pushed[self.down] * 5


       self.x += self.vx
       self.y += self.vy


       if self.x < 0.5 * self.width:
           self.x = 0.5 * self.width
       if self.x > self.screen.get_width() - 0.5 * self.width:
           self.x = self.screen.get_width() - 0.5 * self.width


       if self.y < 0.5 * self.height:
           self.y = 0.5 * self.height
       if self.y > self.screen.get_height() - 0.5 * self.height:
           self.y = self.screen.get_height() - 0.5 * self.height


   def display(self) -> None:
       rect_x = self.x - self.width / 2
       rect_y = self.y - self.height / 2
       pygame.draw.rect(
           self.screen, self.color, (rect_x, rect_y, self.width, self.height)
       )



