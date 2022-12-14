import pygame

from dino_runner.utils.constants import (
    BG,
    FPS,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
)
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
# from dino_runner.components.enemy import Enemy
# from dino_runner.components.game_over import GameOver
from dino_runner.utils.constants import FONT_FAMILY, FONT_SIZE, COLOR_BLACK, COLOR_WHITE, HARD_LVL_GAME, GAME_SPEED
from dino_runner.utils.text_utils import draw_message_component


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.score = 0
        self.running = False
        self.death_count = 0
        self.game_speed = GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 300
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.game_speed = GAME_SPEED
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += HARD_LVL_GAME

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        if not self.player.is_dead:
            self.x_pos_bg -= self.game_speed
        self.draw_score()

    def draw_score(self):
        draw_message_component(
            f"Score: {self.score}",
            self.screen,
            pos_x_center=1000,
            pos_y_center=50,
        )

    def handle_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill(COLOR_WHITE)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message_component("Press any key to start", self.screen)
        else:
            draw_message_component(
                "Press any key to restart",
                self.screen,
                pos_y_center=half_screen_height + 140
            )
            draw_message_component(
                f"Your score: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 150
            )
            draw_message_component(
                f"Death count: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height - 100
            )
            self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 50))

        pygame.display.update()
        self.handle_events_menu()