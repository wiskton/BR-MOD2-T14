import pygame
import random
from dino_runner.utils.constants import SMALL_CACTUS

X_POS = 1400
Y_POS = 245
VEL = 10


class Enemy:
    def __init__(self):
        self.image = SMALL_CACTUS[0]

        self.rect = self.image.get_rect()
        self.rect.x = X_POS
        self.rect.y = Y_POS
        self.rect.width = 8
        self.rect.height = 6
        self.hard = VEL
        self.score = 0

    def update(self, dead):
        if self.rect.x < 0:
            self.image = SMALL_CACTUS[random.randrange(0, 2)]
            self.rect.x = X_POS
            self.hard += 1
            self.score += 10

        if not dead:
            self.rect.x -= self.hard

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))