import pygame


from dino_runner.utils.constants import GAMEOVER


class GameOver:
    def __init__(self):
        self.image = GAMEOVER

        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 50

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))