# Библиотеки
import pygame


class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, color, prev_body, head):
        pygame.sprite.Sprite.__init__(self)

        # Переменные класса
        self.image = pygame.Surface((30, 30))
        self.prev_body = prev_body
        self.wait = prev_body.wait
        self.max_wait = prev_body.max_wait
        self.head_in_hitbox = False
        self.head = head

        # Создание тела
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = self.prev_body.prev_center
        self.prev_center = self.rect.center

    def update(self):
        if self.wait >= max(self.max_wait - self.head.live_time // 50, 4):
            self.prev_center = self.rect.center
            self.rect.center = self.prev_body.prev_center
            if self.head.rect.center == self.rect.center:
                self.head_in_hitbox = True
            self.wait = 0
        else:
            self.wait += 1
