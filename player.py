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
       self.init_x = x
       self.init_y = y

   def touchwall(self, walls: list[Wall]) -> None:
        for w in walls:
            left_edge = w.x - w.width / 2 - self.width*(1/2)
            right_edge = w.x + w.width / 2 + self.width*(1/2)
            top_edge = w.y - w.height / 2 - self.width*(1/2)
            bottom_edge = w.y + w.height / 2 + self.width*(1/2)
            if left_edge < self.x < right_edge and top_edge < self.y < bottom_edge:
                self.x == self.init_x 
                self.y == self.init_y


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
    
 
        self.touchwall([Wall(self.screen, 100, 30, 300, 100),
        Wall(self.screen, 600, 200, 50, 300),
        Wall(self.screen, 100, 800, 50, 500),
        Wall(self.screen, 1000, 50, 300, 800),
        Wall(self.screen, 1200, 700, 400, 200),
        Wall(self.screen, 600, 600, 400, 200),
        Wall(self.screen, 300, 300, 200, 300)])
        

   def display(self) -> None:
       rect_x = self.x - self.width / 2
       rect_y = self.y - self.height / 2
       pygame.draw.rect(
           self.screen, self.color, (rect_x, rect_y, self.width, self.height)
       )



