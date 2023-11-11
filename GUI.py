# Библиотеки
import pygame


class SquareImage(pygame.sprite.Sprite):
    def __init__(self, board_image, width, height):
        pygame.sprite.Sprite.__init__(self)

        # Создание поля
        self.image = board_image
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)


class DeadBlock(pygame.sprite.Sprite):
    def __init__(self, color, size, position):
        pygame.sprite.Sprite.__init__(self)

        # Переменные класса
        self.image = pygame.Surface(size)

        # Создание стены
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def InHitbox(self, head):
        if (self.rect.top <= head.rect.top and head.rect.bottom <= self.rect.bottom and
                self.rect.left <= head.rect.left and head.rect.right <= self.rect.right):
            return True
        return False
