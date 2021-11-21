import pygame
from nlc_dino_runner.utils.constants import ICON_DINO


class DinoMenu:
    def __init__(self):
        self.image = ICON_DINO[0]
        self.step_index = 0

    def draw(self, screen):
        self.image = ICON_DINO[0] if self.step_index > 5 else ICON_DINO[1]
        self.step_index += 1
        screen.blit(self.image, (455, 50))