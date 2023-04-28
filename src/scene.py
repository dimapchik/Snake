from src.levels import *


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

