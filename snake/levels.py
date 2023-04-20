import pygame
from constants import *

class Level:
    def __init__(self):
        self.speed = 5
        self.barriers = []

    def draw_grid(self, screen):
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                if x == 0 or y == 0 or x == WIDTH - CELL_SIZE or y == HEIGHT - CELL_SIZE:
                    rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, RED, rect, CELL_SIZE // 2)
                    self.barriers.append((x // CELL_SIZE, y // CELL_SIZE))

    def set_first_level(self):
        self.speed = 5

    def set_second_level(self):
        self.speed = 10

    def set_third_level(self):
        self.speed = 15

    def set_fourth_level(self):
        self.speed = 20

