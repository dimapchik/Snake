import pygame
from src.menu import Menu, EndMenu, LeaderBoard, Setting
from src.scene import Scene
from src.constants import *


def execute_pause():
    pause = True
    while pause:
        for pause_event in pygame.event.get():
            if pause_event.type == pygame.KEYDOWN:
                if pause_event.key == pygame.K_RETURN:
                    pause = False


class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.scene = Scene()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.end_menu = EndMenu(WIDTH, HEIGHT)
        self.setting_menu = Setting(WIDTH, HEIGHT)
        self.leader_board = LeaderBoard(WIDTH, HEIGHT)
        self.main_menu = Menu(WIDTH, HEIGHT)
        self.main_menu.draw()
        self.name = ""

    def draw_score(self, score):
        font = pygame.font.SysFont('Arial', 15)
        text = font.render("Score: " + str(score), True, BLACK)
        self.screen.blit(text, (5, 5))

    def start_game(self):
        self.scene.reset()
        self.scene.draw_scene()
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
                        execute_pause()

                if game_event.type == pygame.QUIT:
                    game = False
            self.clock.tick(self.scene.levels[self.scene.number_of_level - 1].speed)
            self.scene.levels[self.scene.number_of_level - 1].speed *= 1.002
            score = self.scene.check_eat_food(score)
            (dx, dy) = direction
            self.scene.snake.move(dx, dy)
            self.scene.draw_scene()
            self.draw_score(score)
            if len(self.scene.snake.body) == 0 or self.scene.snake.head in self.scene.levels[self.scene.number_of_level - 1].barriers or \
                    self.scene.snake.is_self_collision():
                game = False
                self.leader_board.add_score(self.name, score)
                self.end_menu.draw(score)
                self.execute_end_menu()
            pygame.display.update()

    def show_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('Arial', size)
        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.center = (x, y)
        self.screen.blit(text, rect)

    def get_name(self):
        while True:
            for name_event in pygame.event.get():
                if name_event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif name_event.type == pygame.KEYDOWN:
                    if name_event.key == pygame.K_RETURN:
                        return self.name
                    elif name_event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]
                    else:
                        self.name += name_event.unicode
            self.screen.fill(WHITE)
            self.show_text("Enter your name:", 50, BLACK, WIDTH // 2, HEIGHT // 2 - 50)
            self.show_text(self.name, 50, BLACK, WIDTH // 2, HEIGHT // 2)
            pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_menu.start_button.collidepoint(event.pos):
                        self.get_name()
                        self.start_game()
                    if self.main_menu.leader_board_button.collidepoint(event.pos):
                        self.execute_leader_board()
                    if self.main_menu.settings_button.collidepoint(event.pos):
                        self.execute_setting_menu()
                if event.type == pygame.QUIT:
                    running = False

    def execute_leader_board(self):
        self.leader_board.draw_top_scores()
        is_leaderboard_open = True
        while is_leaderboard_open:
            for leader_board_event in pygame.event.get():
                if leader_board_event.type == pygame.MOUSEBUTTONDOWN:
                    if self.leader_board.main_menu.collidepoint(leader_board_event.pos):
                        self.main_menu.draw()
                        is_leaderboard_open = False
                if leader_board_event.type == pygame.QUIT:
                    self.main_menu.draw()
                    is_leaderboard_open = False

    def execute_setting_menu(self):
        self.setting_menu.draw()
        setting_is_open = True
        while setting_is_open:
            for setting_event in pygame.event.get():
                if setting_event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(self.setting_menu.count_levels):
                        if self.setting_menu.level_buttons[i].collidepoint(setting_event.pos):
                            self.scene.number_of_level = i + 1
                            setting_is_open = False
                            self.main_menu.draw()
                    if self.setting_menu.main_menu.collidepoint(setting_event.pos):
                        setting_is_open = False
                        self.main_menu.draw()
                if setting_event.type == pygame.QUIT:
                    setting_is_open = False
                    self.main_menu.draw()

    def execute_end_menu(self):
        is_end_menu_open = True
        while is_end_menu_open:
            for end_menu_event in pygame.event.get():
                if end_menu_event.type == pygame.MOUSEBUTTONDOWN:
                    if self.end_menu.retry.collidepoint(end_menu_event.pos):
                        self.scene.reset()
                        self.start_game()
                        is_end_menu_open = False
                    if self.end_menu.main_menu.collidepoint(end_menu_event.pos):
                        self.main_menu.draw()
                        is_end_menu_open = False
                if end_menu_event.type == pygame.QUIT:
                    is_end_menu_open = False
                    self.main_menu.draw()

