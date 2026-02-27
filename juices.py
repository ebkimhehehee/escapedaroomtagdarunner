import pygame

class YAY:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.life = 60        
        self.speed = -1.5      
        self.font = pygame.font.SysFont(None, 40)

    def update(self):
        self.y += self.speed
        self.life -= 1

    def draw(self):
        img = self.font.render("!", True, (255, 255, 0))
        self.screen.blit(img, (self.x, self.y))

    def alive(self):
        return self.life > 0