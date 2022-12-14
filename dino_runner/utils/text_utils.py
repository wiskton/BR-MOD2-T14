import pygame
from dino_runner.utils.constants import (
    FONT_FAMILY,
    FONT_SIZE,
    COLOR_BLACK,
    COLOR_WHITE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


def draw_message_component(
    message,
    screen,
    font_color=COLOR_BLACK,
    font_size=FONT_SIZE,
    pos_x_center=SCREEN_WIDTH // 2,
    pos_y_center=SCREEN_HEIGHT // 2,
):

    font = pygame.font.SysFont(FONT_FAMILY, font_size)
    text = font.render(message, True, font_color)

    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)
