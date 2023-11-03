# Библиотеки
import pygame
import random


class Fruit(pygame.sprite.Sprite):
    def __init__(self, color, plain):
        pygame.sprite.Sprite.__init__(self)

        # Переменные класса
        self.image = pygame.Surface((10, 10))
        self.plain = plain
        self.point = 0

        # Создание фрукта
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(plain[0], plain[1] - 1) // 30 * 30 + 15,
                            random.randint(plain[2], plain[3] - 1) // 30 * 30 + 15)

    def InHitbox(self, object_center):
        if object_center == self.rect.center:
            return True
        return False

    def GetScore(self):
        return self.point


class BadApple(Fruit):
    def __init__(self, color, plain):
        Fruit.__init__(self, color, plain)
        self.point = -100
