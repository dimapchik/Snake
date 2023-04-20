import pygame
import random


class Food:
    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.x = 0
        self.y = 0
        self.randomize_position()

    def draw(self, screen, color):
        rect = pygame.Rect(self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, color, rect)

    def randomize_position(self):
        self.x = random.randint(1, self.screen_width // self.cell_size - 1)
        self.y = random.randint(1, self.screen_height // self.cell_size - 1)