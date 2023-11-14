# Библиотеки
import pygame
import random


class Fruit(pygame.sprite.Sprite):
    def __init__(self, color, plain, coords):
        pygame.sprite.Sprite.__init__(self)

        # Переменные класса
        self.image = pygame.Surface((10, 10))
        self.plain = plain
        self.point = 100

        # Создание фрукта
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (coords[0] * 30 + 15, coords[1] * 30 + 15)

    def InHitbox(self, object_center):
        if object_center == self.rect.center:
            return True
        return False

    def GetScore(self):
        return self.point


class BadApple(Fruit):
    def __init__(self, color, plain, coords):
        Fruit.__init__(self, color, plain, coords)
        self.point = -300


class GoldenApple(Fruit):
    def __init__(self, color, plain, coords):
        Fruit.__init__(self, color, plain, coords)
        self.point = 300
