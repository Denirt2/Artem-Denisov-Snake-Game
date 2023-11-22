import pygame
from pygame.sprite import Sprite


class Fruit(Sprite):
    def __init__(self, color, plain, coords):
        super().__init__()

        # Переменные класса
        self.image = pygame.Surface((10, 10))
        self.plain = plain
        self.point = 100

        # Создание фрукта
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (coords[0] * 30 + 15, coords[1] * 30 + 15)

    def in_hitbox(self, object_center):
        return object_center == self.rect.center

    def GetScore(self):
        return self.point


class BadApple(Fruit):
    def __init__(self, color, plain, coords):
        super().__init__(color, plain, coords)
        self.point = -300


class GoldenApple(Fruit):
    def __init__(self, color, plain, coords):
        super().__init__(color, plain, coords)
        self.point = 300
