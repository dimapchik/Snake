import pygame
import random

class Food:
    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.x = 0
        self.y = 0
        self.color = (0, 255, 0)
        self.randomize_position()

    def draw(self, surface):
        rect = pygame.Rect(self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(surface, self.color, rect)

    def randomize_position(self):
        self.x = random.randint(1, self.screen_width // self.cell_size - 2)
        self.y = random.randint(1, self.screen_height // self.cell_size - 2)