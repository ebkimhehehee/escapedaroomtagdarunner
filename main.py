import sys


import pygame
import pygame.locals


from player import Player
from walls import Wall




def main():
   fps = 60
   fps_clock = pygame.time.Clock()
   pygame.init()
   screen = pygame.display.set_mode((1400, 800))


   # font = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 40)


   p_one = Player(
       screen,
       screen.get_width() / 2,
       screen.get_height() / 2,
       pygame.K_w,
       pygame.K_s,
       pygame.K_a,
       pygame.K_d,
       "#FF0000",
   )
   # left_score = 0


   p_two = Player(
       screen,
       screen.get_width() / 2,
       screen.get_height() / 2,
       pygame.K_UP,
       pygame.K_DOWN,
       pygame.K_LEFT,
       pygame.K_RIGHT,
       "#0026FF",
   )
   # right_score = 0


   walls = [Wall(screen) for i in range(100)]


   while True:
       screen.fill("#000000")


       for event in pygame.event.get():
           if event.type == pygame.locals.QUIT:
               pygame.quit()
               sys.exit()


           p_one.update()
           p_one.display()
           p_two.update()
           p_two.display()


           for w in walls:
               w.display()


       pygame.display.flip()
       fps_clock.tick(fps)




if __name__ == "__main__":
   main()



