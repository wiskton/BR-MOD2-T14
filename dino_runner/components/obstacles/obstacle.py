import pygame
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.utils import fix_rect


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, image, _type):
        self.type = _type
        self.image = image
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.size = fix_rect(self.rect, 0.70)

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
