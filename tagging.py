from player import Player
from sound import alarmed
import pygame
ahsound = None

def tagged(runner, tagger):
    global ahsound

    if ahsound is None:
        ahsound = pygame.mixer.Sound("alarm.wav")

    left_edge = tagger.x - tagger.width / 2 - runner.width * (1 / 2)
    right_edge = tagger.x + tagger.width / 2 + runner.width * (1 / 2)
    top_edge = tagger.y - tagger.height / 2 - runner.width * (1 / 2)
    bottom_edge = tagger.y + tagger.height / 2 + runner.width * (1 / 2)


    if left_edge < runner.x < right_edge and top_edge < runner.y < bottom_edge:
        if not pygame.mixer.get_busy():
            ahsound.play()
        runner.x = runner.init_x
        runner.y = runner.init_y
        tagger.x = tagger.init_x
        tagger.y = tagger.init_y
        return True
    
    

    return False