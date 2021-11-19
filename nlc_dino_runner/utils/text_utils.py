import pygame
from nlc_dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

text_color = (0, 0, 0)
font_style = 'freesansbold.ttf'


def get_score_element(points):
    font = pygame.font.Font(font_style, 22)
    text = font.render('Points : ' + str(points), True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 25)
    return text, text_rect


def get_centered_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2):
    font = pygame.font.Font(font_style, 30)
    text = font.render(message, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect