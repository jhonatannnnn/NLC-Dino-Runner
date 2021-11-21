import pygame
from nlc_dino_runner.utils.constants import (SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE, BLACK_COLOR, IMG_DIR)


def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)
    text = font.render('Points: ' + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1000, 25)
    return text, text_rect


def get_centered_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT// 2, size=30):
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect


def emitir_sonido(name_sound):
    path = IMG_DIR + str("/") + name_sound
    sonido_fondo = pygame.mixer.Sound(path)
    pygame.mixer.Sound.play(sonido_fondo)