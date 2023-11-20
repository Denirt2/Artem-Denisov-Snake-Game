import pygame
from pygame.sprite import Sprite


class SnakeHead(Sprite):
    def __init__(self, color, plain):
        super().__init__()

        # Переменные класса
        self.image = pygame.Surface((30, 30))
        self.plain = plain
        self.speed = 30
        self.x_speed = 0
        self.y_speed = -self.speed
        self.wait = 0
        self.max_wait = 10
        self.max_wait_limit = 4
        self.is_live = True
        self.live_time = 0

        # Создание головы
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = ((self.plain[1] + self.plain[0]) // 2, (self.plain[3] + self.plain[2]) // 2)
        self.prev_center = self.rect.center

    def turn_down(self):
        self.x_speed = 0
        self.y_speed = self.speed

    def turn_up(self):
        self.x_speed = 0
        self.y_speed = -self.speed

    def turn_right(self):
        self.x_speed = self.speed
        self.y_speed = 0

    def turn_left(self):
        self.x_speed = -self.speed
        self.y_speed = 0

    def update(self):
        if self.wait >= max(self.max_wait - self.live_time // 50, self.max_wait_limit):
            if self.rect.left + self.x_speed >= self.plain[1] or self.rect.right + self.x_speed <= self.plain[0]:
                self.is_live = False
            elif self.rect.bottom + self.y_speed <= self.plain[2] or self.rect.top + self.y_speed >= self.plain[3]:
                self.is_live = False
            else:
                self.prev_center = self.rect.center
                self.rect.x += self.x_speed
                self.rect.y += self.y_speed
                self.wait = 0
                self.live_time += 1
        else:
            self.wait += 1


class SnakeHeadEasy(SnakeHead):
    def update(self):
        if self.wait >= max(self.max_wait - self.live_time // 50, self.max_wait_limit):
            if self.rect.left + self.x_speed >= self.plain[1]:
                self.rect.left = self.plain[0]
            elif self.rect.right + self.x_speed <= self.plain[0]:
                self.rect.right = self.plain[1]
            elif self.rect.bottom + self.y_speed <= self.plain[2]:
                self.rect.bottom = self.plain[3]
            elif self.rect.top + self.y_speed >= self.plain[3]:
                self.rect.top = self.plain[2]
            else:
                self.prev_center = self.rect.center
                self.rect.x += self.x_speed
                self.rect.y += self.y_speed
            self.wait = 0
            self.live_time += 1
        else:
            self.wait += 1
