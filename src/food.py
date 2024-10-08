import pygame
import random
from src.constants import *


class Food:
    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.x = 0
        self.y = 0
        self.randomize_position()
        self.color = GREEN
        self.spawn_rate = 1

    def draw(self, screen):
        rect = pygame.Rect(self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, self.color, rect)

    def randomize_position(self):
        self.x = random.randint(1, self.screen_width // self.cell_size - 1)
        self.y = random.randint(1, self.screen_height // self.cell_size - 1)

    def apply_to_snake(self, snake):
        snake.grow()


class GoodFood(Food):
    def __init__(self, width, height, cell_size):
        super().__init__(width, height, cell_size)
        self.color = GREEN
        self.spawn_rate = 1


class DecreaseFood(Food):
    def __init__(self, width, height, cell_size):
        super().__init__(width, height, cell_size)
        self.color = BROWN
        self.spawn_rate = 10

    def apply_to_snake(self, snake):
        snake.de_grow()
