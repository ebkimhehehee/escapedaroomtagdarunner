import pygame
from player import Player
pygame.mixer.pre_init(44100, -16, 2, 2048) 
pygame.init()

ahsound = pygame.mixer.Sound("alarm.wav")

def alarmed(runner:Player, tagger: Player) -> bool:
   left_edge = tagger.x - tagger.width / 2 - 4
   right_edge = tagger.x + tagger.width / 2 + 4
   top_edge = tagger.y - tagger.height / 2 - 4
   bottom_edge = tagger.y + tagger.height / 2 + 4
   if left_edge < runner.x < right_edge and top_edge < runner.y < bottom_edge:
        ahsound.play()
   return False
