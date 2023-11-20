import os
import random

import pygame
import pygame_menu

# Некоторые переменные
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, '../images')
clock = pygame.time.Clock()

# Используемые изображения
board_image = pygame.image.load(os.path.join(img_folder, 'Board.png'))

# Используемые цвета
head_color = (75, 0, 130)  # Indigo
fruit_color = (178, 34, 34)  # FireBrick
bad_apple_color = (128, 128, 0)  # Olive
golden_apple_color = (255, 215, 0)  # Gold
screen_color = (70, 130, 180)  # SteelBlue
body_color_first = (186, 85, 211)  # MediumOrchid
body_color_second = (138, 43, 226)  # BlueViolet
text_color = (0, 0, 0)  # Black
block_color = (139, 69, 19)  # SaddleBrown
