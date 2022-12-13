import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.dinosaur import Y_POS
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


CACTUS = [
    (LARGE_CACTUS, Y_POS - 5),
    (SMALL_CACTUS, Y_POS + 20),
]


class Cactus(Obstacle):

    def __init__(self):
        image, cactus_pos = CACTUS[random.randint(0, 1)]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = cactus_pos
