import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DEAD

X_POS = 80
Y_POS = 220
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.jump_vel = JUMP_VEL
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.is_dead = False

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]

        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 1

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        pass

    def dead(self):
        self.image = DEAD

    def update(self, user_input, rect_enemy):
        if self.is_dead:
            self.dead()
        else:

            if self.dino_run:
                self.run()
            elif self.dino_jump:
                self.jump()

            if not self.dino_jump and user_input[pygame.K_UP] or user_input[pygame.K_SPACE]:
                self.dino_jump = True
                self.dino_run = False
            elif not self.dino_jump:
                self.dino_jump = False
                self.dino_run = True

            if self.step_index >= 10:
                self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))