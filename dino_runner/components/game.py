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
from dino_runner.components.enemy import Enemy
from dino_runner.components.game_over import GameOver
from dino_runner.utils.constants import FONT_FAMILY, FONT_SIZE


BLACK = (0, 0, 0)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 300
        self.player = Dinosaur()
        self.enemy = Enemy()
        self.game_over = GameOver()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def score(self, points):
        font = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)
        text = font.render('SCORE: {}'.format(points), True, BLACK)
        self.screen.blit(text, (20, 20))

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.enemy.rect)
        self.enemy.update(self.player.is_dead)
        self.game_over.update()
        self.checkCollision(self.player, self.enemy)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        if self.player.is_dead:
            self.game_over.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def checkCollision(self, sprite1, sprite2):
        col = sprite1.dino_rect.colliderect(sprite2.rect)
        if col == True:
            self.player.is_dead = True

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        if not self.player.is_dead:
            self.x_pos_bg -= self.game_speed
        self.score(self.enemy.score)
