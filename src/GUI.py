import pygame
from pygame.sprite import Sprite


class SquareImage(Sprite):
    def __init__(self, board_image, width, height):
        super().__init__()

        # Создание поля
        self.image = board_image
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)


class DeadBlock(Sprite):
    def __init__(self, color, size, position):
        super().__init__()

        # Переменные класса
        self.image = pygame.Surface(size)

        # Создание стены
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def in_hitbox(self, head):
        return (self.rect.top <= head.rect.top and head.rect.bottom <= self.rect.bottom and
                self.rect.left <= head.rect.left and head.rect.right <= self.rect.right)
