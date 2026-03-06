import pygame

from levels import Level
from player import Player


class Transition_level:

    def __init__(self, screen: pygame.Surface, level: int, runner: Player) -> None:
        self.screen = screen
        self.level = f"LEVEL {level}"
        self.play = "press start to continue"
        if runner.color == (255, 0, 0):
            self.runner = "REDDIE IS RUNNER"
            self.tagger = "BLU IS TAGGER"
            self.run_color = "#ff0000"
            self.tag_color = "#0026ff"
        else:
            self.runner = "BLU IS RUNNER"
            self.tagger = "REDDIE IS TAGGER"
            self.run_color = "#0026ff"
            self.tag_color = "#ff0000"
        self.reddiescore = 0
        self.bluscore = 0

        self.fontscore = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 40)
        self.fontlevel = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 200)
        self.fontplay = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 40)
        self.fontrun_tag = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 60)

    def update(self, runner: Player):
        self.screen.fill("#000000")

        level_image = self.fontlevel.render(f"{self.level}", True, "#ffffff")
        play_image = self.fontplay.render(f"{self.play}", True, "#ffffff")
        runner_image = self.fontrun_tag.render(f"{self.runner}", True, self.run_color)
        tagger_image = self.fontrun_tag.render(f"{self.tagger}", True, self.tag_color)
        reddiescore_image = self.fontplay.render(f"{self.reddiescore}", True, "#ff0000")
        bluscore_image = self.fontplay.render(f"{self.bluscore}", True, "#0026ff")

        self.screen.blit(level_image, (450, 150))
        self.screen.blit(play_image, (570, 700))
        self.screen.blit(
            runner_image,
            (self.screen.get_width() / 4 - runner_image.get_width() / 2, 400),
        )
        self.screen.blit(
            tagger_image,
            (self.screen.get_width() * 0.75 - runner_image.get_width() / 2, 400),
        )
        if runner.color == (255, 0, 0):
            self.screen.blit(
                reddiescore_image,
                (self.screen.get_width() / 4 - reddiescore_image.get_width() / 2, 500),
            )
            self.screen.blit(
                bluscore_image,
                (
                    self.screen.get_width() * 0.75 + reddiescore_image.get_width() / 2,
                    500,
                ),
            )
        else:
            self.screen.blit(
                reddiescore_image,
                (
                    self.screen.get_width() * 0.75 + reddiescore_image.get_width() / 2,
                    500,
                ),
            )
            self.screen.blit(
                bluscore_image,
                (self.screen.get_width() / 4 - reddiescore_image.get_width() / 2, 500),
            )


def init_t1(screen: pygame.Surface, level: int, runner: Player) -> Transition_level:
    return Transition_level(screen, level, runner)


def init_t2(screen: pygame.Surface, level: int, runner: Player) -> Transition_level:
    return Transition_level(screen, level, runner)


def init_t3(screen: pygame.Surface, level: int, runner: Player) -> Transition_level:
    return Transition_level(screen, level, runner)


def init_t4(screen: pygame.Surface, level: int, runner: Player) -> Transition_level:
    return Transition_level(screen, level, runner)

def init_t5(screen: pygame.Surface, level: int, runner: Player) -> Transition_level:
    return Transition_level(screen, level, runner)

def init_t6(screen: pygame.Surface, level: int, runner: Player) -> Transition_level:
    return Transition_level(screen, level, runner)
