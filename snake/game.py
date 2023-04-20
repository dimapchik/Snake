import pygame
from menu import *
from snake import *
from food import *

pygame.init()
clock = pygame.time.Clock()
speed = 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
end_menu = EndMenu(WIDTH, HEIGHT)
setting_menu = Setting(WIDTH, HEIGHT)
leader_board = LeaderBoard(WIDTH, HEIGHT)
main_menu = Menu(WIDTH, HEIGHT)
main_menu.draw()

barrier = []
for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            if x == 0 or y == 0 or x == WIDTH - CELL_SIZE or y == HEIGHT - CELL_SIZE:
                barrier.append((x // CELL_SIZE, y // CELL_SIZE))


def draw_score(score):
    font = pygame.font.SysFont('Arial', 15)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (5, 5))


def draw_grid(screen):
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            if x == 0 or y == 0 or x == WIDTH - CELL_SIZE or y == HEIGHT - CELL_SIZE:
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, RED, rect, CELL_SIZE // 2)


def set_first_level():
    global speed
    speed = 5


def set_second_level():
    global speed
    speed = 10


def set_third_level():
    global speed
    speed = 15


def set_fourth_level():
    global speed
    speed = 20


def start_game(speed):
    direction = RIGHT
    food = Food(WIDTH, HEIGHT, CELL_SIZE)
    count_of_food = 0
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    draw_grid(screen)
    score = 0
    snake = Snake(CELL_SIZE // 2, CELL_SIZE // 2)
    direction = RIGHT
    game = True
    while game:
        for game_event in pygame.event.get():
            if game_event.type == pygame.KEYDOWN:
                if game_event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif game_event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif game_event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif game_event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

            if game_event.type == pygame.QUIT:
                game = False
        clock.tick(speed)
        if count_of_food == 0:
            food = Food(WIDTH, HEIGHT, CELL_SIZE)
            while (food.x, food.y) in snake.body:
                food = Food(WIDTH, HEIGHT, CELL_SIZE)
            food.draw(screen)
            count_of_food += 1
            speed += 1
        if snake.is_collision(food.x, food.y):
            snake.grow()
            count_of_food = 0
            score += 1
        (dx, dy) = direction
        snake.move(dx, dy)
        screen.fill(WHITE)
        draw_grid(screen)
        food.draw(screen)
        draw_score(score)
        snake.draw(screen)
        if snake.head in barrier:
            game = False
            leader_board.add_score("aaa", score)
            end_menu.draw(score)
        if snake.is_self_collision():
            game = False
            leader_board.add_score("aaa", score)
            end_menu.draw(score)
        pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.start_button.collidepoint(event.pos):
                start_game(speed)
            if main_menu.leader_board_button.collidepoint(event.pos):
                leader_board.draw_top_scores(screen)
            if main_menu.settings_button.collidepoint(event.pos):
                setting_menu.draw()
            if setting_menu.first_level.collidepoint(event.pos):
                set_first_level()
                main_menu.draw()
            if setting_menu.second_level.collidepoint(event.pos):
                set_second_level()
                main_menu.draw()
            if setting_menu.third_level.collidepoint(event.pos):
                set_third_level()
                main_menu.draw()
            if setting_menu.fourth_level.collidepoint(event.pos):
                set_fourth_level()
                main_menu.draw()
            if end_menu.retry.collidepoint(event.pos):
                start_game(speed)
            if end_menu.main_menu.collidepoint(event.pos):
                main_menu.draw()
            if leader_board.main_menu.collidepoint(event.pos):
                main_menu.draw()
        if event.type == pygame.QUIT:
            running = False

