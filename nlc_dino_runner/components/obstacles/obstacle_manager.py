import pygame
import pygame.time
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
                if not game.player.shield:
                    game.player_heart_manager.redece_heart()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000

                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                break
            else:
                self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []