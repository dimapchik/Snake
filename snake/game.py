import pygame
from menu import *
from snake import *
from food import *
from levels import *

pygame.init()
clock = pygame.time.Clock()
level = Level()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
end_menu = EndMenu(WIDTH, HEIGHT)
setting_menu = Setting(WIDTH, HEIGHT)
leader_board = LeaderBoard(WIDTH, HEIGHT)
main_menu = Menu(WIDTH, HEIGHT)
main_menu.draw()
name = ""


def draw_score(score):
    font = pygame.font.SysFont('Arial', 15)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (5, 5))



def start_game(speed):
    # bad_food = Food(WIDTH, HEIGHT, CELL_SIZE)
    # count_of_bad_food = 0
    level = Level()
    level.draw_level()
    score = 0
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
        clock.tick(level.speed)
        level.speed *= 1.002
        if level.count_of_good_food == 0:
            level.good_food = Food(WIDTH, HEIGHT, CELL_SIZE)
            while (level.good_food.x, level.good_food.y) in level.snake.body or (level.good_food.x, level.good_food.y) in level.barriers:
                level.good_food = Food(WIDTH, HEIGHT, CELL_SIZE)
            level.count_of_good_food += 1
            # if count_of_bad_food == 0 and random.randint(1, 3) == 1:
            #     bad_food = Food(WIDTH, HEIGHT, CELL_SIZE)
            #     while bad_food in snake.body:
            #         bad_food = Food(WIDTH, HEIGHT, CELL_SIZE)
            #     count_of_bad_food += 1
        if level.snake.is_collision(level.good_food.x, level.good_food.y):
            level.snake.grow()
            level.count_of_good_food = 0
            score += 1
        # if snake.is_collision(bad_food.x, bad_food.y):
        #     snake.de_grow()
        #     count_of_bad_food = 0
        (dx, dy) = direction
        level.snake.move(dx, dy)
        level.draw_level()
        # if level.with_bad_food:
        #     bad_food.draw(screen, BROWN)
        draw_score(score)
        if level.snake.head in level.barriers:
            game = False
            leader_board.add_score(name, score)
            end_menu.draw(score)
        if level.snake.is_self_collision():
            game = False
            leader_board.add_score(name, score)
            end_menu.draw(score)
        pygame.display.update()


def show_text(text, size, color, x, y):
    font = pygame.font.SysFont('Arial', size)
    text = font.render(text, True, color)
    rect = text.get_rect()
    rect.center = (x, y)
    screen.blit(text, rect)


def get_name():
    global name
    while True:
        for name_event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif name_event.type == pygame.KEYDOWN:
                if name_event.key == pygame.K_RETURN:
                    return name
                elif name_event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += name_event.unicode
        screen.fill(WHITE)
        show_text("Enter your name:", 50, BLACK, WIDTH // 2, HEIGHT // 2 - 50)
        show_text(name, 50, BLACK, WIDTH // 2, HEIGHT // 2)
        pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.start_button.collidepoint(event.pos):
                get_name()
                start_game(level.speed)
            if main_menu.leader_board_button.collidepoint(event.pos):
                leader_board.draw_top_scores(screen)
            if main_menu.settings_button.collidepoint(event.pos):
                setting_menu.draw()
            if setting_menu.first_level.collidepoint(event.pos):
                level.set_first_level()
                main_menu.draw()
            if setting_menu.second_level.collidepoint(event.pos):
                level.set_second_level()
                main_menu.draw()
            if setting_menu.third_level.collidepoint(event.pos):
                level.set_third_level()
                main_menu.draw()
            if setting_menu.fourth_level.collidepoint(event.pos):
                level.set_fourth_level()
                main_menu.draw()
            if end_menu.retry.collidepoint(event.pos):
                start_game(level.speed)
            if end_menu.main_menu.collidepoint(event.pos):
                main_menu.draw()
            if leader_board.main_menu.collidepoint(event.pos):
                main_menu.draw()
        if event.type == pygame.QUIT:
            running = False

