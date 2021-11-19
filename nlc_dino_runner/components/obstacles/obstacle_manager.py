import pygame

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS


class ObstacleManager:

    def __init__(self) -> object:
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.points = 0
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []