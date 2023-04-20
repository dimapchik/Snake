import pygame
from constants import *


class Level:
    def __init__(self):
        self.speed = 5
        self.barriers = []
        self.with_bad_food = False

    def draw_level(self, screen):
        for x, y in self.barriers:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, RED, rect, CELL_SIZE // 2)

    def set_first_level(self):
        self.speed = 5

    def set_second_level(self):
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                if x == 0 or y == 0 or x == WIDTH - CELL_SIZE or y == HEIGHT - CELL_SIZE:
                    self.barriers.append((x // CELL_SIZE, y // CELL_SIZE))

    def set_third_level(self):
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                if x == 0 or x == WIDTH - CELL_SIZE:
                    self.barriers.append((x // CELL_SIZE, y // CELL_SIZE))
        self.speed = 10

    def set_fourth_level(self):
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT ):
                if (x == WIDTH // 2 and HEIGHT // 3 > y) or (y == HEIGHT * 5 // 7 and x > WIDTH * 4 / 5):
                    self.barriers.append((x // CELL_SIZE, y // CELL_SIZE))
        self.with_bad_food = True
        self.speed = 10

