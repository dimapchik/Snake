from snake import *
from food import *


class Scene:
    def __init__(self):
        self.all_food = []
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.snake = Snake(WIDTH // CELL_SIZE // 2, HEIGHT // CELL_SIZE // 2)
        self.levels = []
        for i in range(6):
            self.levels.append(Level(i + 1))
        self.number_of_level = 1

    def reset(self):
        self.snake = Snake(WIDTH // CELL_SIZE // 2, HEIGHT // CELL_SIZE // 2)
        food_1 = GoodFood(WIDTH, HEIGHT, CELL_SIZE)
        food_2 = DecreaseFood(WIDTH, HEIGHT, CELL_SIZE)
        self.all_food = [food_1, food_2]
        if self.number_of_level == 1 or self.number_of_level == 2:
            self.levels[self.number_of_level - 1].speed = 5
        elif self.number_of_level == 3 or self.number_of_level == 4:
            self.levels[self.number_of_level - 1].speed = 10
        else:
            self.levels[self.number_of_level - 1].speed = 15

    def check_eat_food(self, score):
        for food in self.all_food:
            if self.snake.is_collision(food.x, food.y):
                food.apply_to_snake(self.snake)
                self.all_food.remove(food)
                if food.__class__ == GoodFood:
                    good_food = GoodFood(WIDTH, HEIGHT, CELL_SIZE)
                    while good_food in self.levels[self.number_of_level - 1].barriers:
                        good_food = GoodFood(WIDTH, HEIGHT, CELL_SIZE)
                    self.all_food.append(good_food)
                    score += 1
                elif food.__class__ == DecreaseFood:
                    bad_food = DecreaseFood(WIDTH, HEIGHT, CELL_SIZE)
                    while bad_food in self.levels[self.number_of_level - 1].barriers:
                        bad_food = DecreaseFood(WIDTH, HEIGHT, CELL_SIZE)
                    self.all_food.append(bad_food)
        return score

    def draw_scene(self):
        self.screen.fill(WHITE)
        for x, y in self.levels[self.number_of_level - 1].barriers:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, RED, rect, CELL_SIZE // 2)
        for food in self.all_food:
            food.draw(self.screen)
        self.snake.draw(self.screen)


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
            self.set_first_level()
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

