from menu import *
from levels import *

pygame.init()
clock = pygame.time.Clock()
scene = Scene()
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


def start_game():
    scene.reset()
    scene.draw_scene()
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
                elif game_event.key == pygame.K_ESCAPE:
                    game = False

            if game_event.type == pygame.QUIT:
                game = False
        clock.tick(scene.levels[scene.number_of_level - 1].speed)
        scene.levels[scene.number_of_level - 1].speed *= 1.002
        score = scene.check_eat_food(score)
        (dx, dy) = direction
        scene.snake.move(dx, dy)
        scene.draw_scene()
        draw_score(score)
        if len(scene.snake.body) == 0 or scene.snake.head in scene.levels[scene.number_of_level - 1].barriers or \
                scene.snake.is_self_collision():
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
                start_game()
            if main_menu.leader_board_button.collidepoint(event.pos):
                leader_board.draw_top_scores()
            if main_menu.settings_button.collidepoint(event.pos):
                setting_menu.draw()
            for i in range(setting_menu.count_levels):
                if setting_menu.level_buttons[i].collidepoint(event.pos):
                    scene.number_of_level = i + 1
                    main_menu.draw()
            if end_menu.retry.collidepoint(event.pos):
                scene.reset()
                start_game()
            if end_menu.main_menu.collidepoint(event.pos):
                main_menu.draw()
            if leader_board.main_menu.collidepoint(event.pos):
                main_menu.draw()
        if event.type == pygame.QUIT:
            running = False
