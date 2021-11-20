import pygame

from nlc_dino_runner.components.dinosaurio import Dinosaur
from nlc_dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.utils.constants import (
    TITTLE,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    COLOR,
    BG,
    FPS
)


class Game:
    def __init__(self):
        pygame.init()
        self.playing = False
        self.running = False
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.x_pos_bg = 0
        self.y_pos_bg = 420
        self.game_speed = 15
        self.x_pos_image = SCREEN_WIDTH // 2
        self.y_pos_image = SCREEN_HEIGHT // 4
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle = ObstacleManager()
        self.points = 0
        self.points_accountant = 0
        self.running = True
        self.death_count = 0
        self.power_up_manager = PowerUpManager()

    def score(self):
        self.points += 1
        self.points_accountant += 1
        if self.points_accountant == 500:
            self.game_speed += 5
            self.points_accountant = 0
        score_element, score_element_rec = text_utils.get_score_element(self.points)
        self.player.check_invincibility(self.screen)
        self.screen.blit(score_element, score_element_rec)

    def show_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        width = SCREEN_WIDTH // 2
        height = SCREEN_HEIGHT // 4
        if self.death_count == 0:
            text_element, text_element_rec = text_utils.get_centered_message('Press any kay to start')
            self.screen.blit(text_element, text_element_rec)
        else:
            text_element, text_element_rec = text_utils.get_centered_message('Press any kay to Restart')
            self.screen.blit(text_element, text_element_rec)
            text_element, text_element_rec = text_utils.get_centered_message('Muertes: ' + str(self.death_count),
                                                                             height=height + 200)
            text_element_p, text_element_rec_p = text_utils.get_centered_message('Puntos: ' + str(self.points_accountant),
                                                                             height=height + 250)
            self.screen.blit(text_element, text_element_rec)
            self.screen.blit(text_element_p, text_element_rec_p)
        self.screen.blit(ICON, (width, height))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        self.points = 0
        self.obstacle.reset_obstacles()
        self.playing = True
        self.create_components()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(COLOR)
        self.player.draw(self.screen)
        self.draw_background()
        self.obstacle.draw(self.screen)
        self.score()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_with = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_with:
            self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def create_components(self):
        self.obstacle.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)