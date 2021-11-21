from nlc_dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite


class Obstacle(Sprite):

    def __init__(self, image, index):
        self.image = image
        self.index = index
        self.rect = self.image[self.index].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.cactus_speed = 15
        self.time = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width and obstacles:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.index], self.rect)