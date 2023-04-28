from src.snake import *
from src.food import *


class Level:
    def __init__(self, number_of_level):
        self.speed = 5
        self.barriers = []
        if number_of_level == 1:
            self.set_first_level()
        elif number_of_level == 2:
            self.set_second_level()
        elif number_of_level == 3:
            self.set_third_level()
        elif number_of_level == 4:
            self.set_fourth_level()
        else:
            self.set_fifth_level()

    def set_first_level(self):
        self.barriers.clear()
        self.speed = 5

    def set_second_level(self):
        self.barriers.clear()
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                if x == 0 or y == 0 or x == WIDTH - CELL_SIZE or y == HEIGHT - CELL_SIZE:
                    self.barriers.append((x // CELL_SIZE, y // CELL_SIZE))

    def set_third_level(self):
        self.barriers.clear()
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                if x == 0 or x == WIDTH - CELL_SIZE:
                    self.barriers.append((x // CELL_SIZE, y // CELL_SIZE))
        self.speed = 10

    def set_fourth_level(self):
        self.barriers.clear()
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                if (x == WIDTH // 2 and HEIGHT // 3 > y) or (y == HEIGHT * 5 // 7 and x > WIDTH * 4 / 5):
                    self.barriers.append((x // CELL_SIZE, y // CELL_SIZE))
        self.speed = 10

    def set_fifth_level(self):
        self.barriers.clear()
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                if (x == WIDTH // 3 and HEIGHT // 3 < y < HEIGHT * 2 // 3)\
                        or (y == HEIGHT * 2 // 3 and WIDTH // 3 < x < WIDTH * 2 // 3)\
                        or (x == WIDTH * 2 // 3 and 3 < y < HEIGHT * 2 // 3):
                    self.barriers.append((x // CELL_SIZE, y // CELL_SIZE))
        self.speed = 15

