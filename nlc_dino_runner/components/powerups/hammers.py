from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HAMMER, SCREEN_WIDTH


class Hammers(Sprite):
    def __init__(self, x, y):
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.center.x = x
        self.rect.bottom = y
        self.speedy = 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speedy
        if self.rect.left < SCREEN_WIDTH:
            self.kill()
