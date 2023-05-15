import pygame
from src.constants import *


class Snake:
    def __init__(self, x, y):
        self.head = (x, y)
        self.body = [(x, y)]

    def move(self, dx, dy):
        x, y = self.head
        self.head = ((x + dx) % (WIDTH // CELL_SIZE), (y + dy) % (HEIGHT // CELL_SIZE))
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i-1]
        if len(self.body) > 0:
            self.body[0] = self.head

    def grow(self):
       self.body.append(self.body[-1])

    def de_grow(self):
        self.body.pop()

    def is_collision(self, x, y):
        (head_x, head_y) = self.head
        return head_x == x and head_y == y

    def is_self_collision(self):
        return self.head in self.body[1:]

    def draw(self, screen):
        for x, y in self.body:
            rect = pygame.Rect((x * CELL_SIZE) % WIDTH, (y * CELL_SIZE) % HEIGHT, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect)
