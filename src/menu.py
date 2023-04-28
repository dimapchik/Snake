import pygame
from src.constants import *


class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.delta = width / 10
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Arial', 30)
        self.title = self.font.render('Snake Game', True, BLACK)
        self.start_button = pygame.Rect(self.width / 3, self.height / 3, self.width * 3 / 8, self.delta)
        self.settings_button = pygame.Rect(self.width / 3, self.height / 2, self.width * 3 / 8, self.delta)
        self.leader_board_button = pygame.Rect(self.width / 3, self.height * 2 / 3, self.width * 3 / 8, 2 * self.delta)

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.title, (self.width/2-70, self.height/4))
        pygame.draw.rect(self.screen, RED, self.start_button)
        pygame.draw.rect(self.screen, GREEN, self.settings_button)
        pygame.draw.rect(self.screen, BLUE, self.leader_board_button)
        start_text = self.font.render('Start', True, BLACK)
        settings_text = self.font.render('Settings', True, BLACK)
        leader_board_text = self.font.render("Leader \n board", True, BLACK)
        self.screen.blit(start_text, (self.width / 3 + self.delta, self.height / 3 + self.delta / 5))
        self.screen.blit(settings_text, (self.width / 3 + self.delta, self.height / 2 + self.delta / 5))
        self.screen.blit(leader_board_text, (self.width / 3 + self.delta, self.height * 2 / 3 + self.delta / 5))
        pygame.display.update()


class EndMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.delta = width / 10  # shift for text
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Arial', 20)
        self.title = self.font.render('Wasted!', True, BLACK)
        self.retry = pygame.Rect(self.width / 3, self.height * 2 / 3, width / 3, height // 17)
        self.main_menu = pygame.Rect(self.width / 3, self.height * 3 / 4, width / 3, height // 15)

    def draw(self, score):
        self.screen.fill(WHITE)
        self.screen.blit(self.title, (self.width * 2 / 5, self.height / 4))
        pygame.draw.rect(self.screen, RED, self.retry)
        pygame.draw.rect(self.screen, RED, self.main_menu)
        retry_text = self.font.render('Retry', True, BLACK)
        score_text = self.font.render('Your score: ' + str(score), True, BLACK)
        main_menu_text = self.font.render('Main menu', True, BLACK)
        self.screen.blit(retry_text, (self.width / 3 + self.delta, self.height * 2 / 3 + 5))
        self.screen.blit(score_text, (self.width / 3 + self.delta, self.height / 2))
        self.screen.blit(main_menu_text, (self.width / 3 + self.delta, self.height * 3 / 4 + 5))
        pygame.display.update()


class Setting:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Arial', 20)
        self.delta = width / 50
        self.title = self.font.render('Settings', True, BLACK)
        self.level_buttons = []
        self.count_levels = 5
        self.main_menu = pygame.Rect(self.width / 10, height / 10, self.width / 5, width / 25)
        for i in range(self.count_levels):
            self.level_buttons.append(pygame.Rect(self.width * (i + 1) / (self.count_levels + 1), self.height * 2 / 3,
                                                  width / 10, width / 10))

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.title, (self.width/2, self.height/4))
        for i in range(self.count_levels):
            pygame.draw.rect(self.screen, GREEN, self.level_buttons[i])
            level_text = self.font.render(f'{i + 1} level', True, BLACK)
            self.screen.blit(level_text, (self.width * (i + 1) / (self.count_levels + 1), self.height * 2 / 3))
        pygame.draw.rect(self.screen, RED, self.main_menu)
        main_menu_text = self.font.render('Back', True, BLACK)
        self.screen.blit(main_menu_text, (self.width / 10 + self.delta, self.height / 10 + self.delta / 5))
        pygame.display.update()


class LeaderBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.delta = width / 50
        self.font = pygame.font.SysFont('Arial', 20)
        self.title = self.font.render('Leader Board', True, BLACK)
        self.main_menu = pygame.Rect(self.width / 10, height / 10, self.width / 5, width / 25)
        self.positions = dict()
        for i in range(1, 6):
            self.positions['position_%s' % i] = pygame.Rect(self.width / 3, self.height / 2 + self.height * i / 5,
                                                            self.width / 4, width / 25)
        self.scores = []

    def add_score(self, name, score):
        self.scores.append((name, score))

    def get_top_scores(self, num_scores):
        sorted_scores = sorted(self.scores, key=lambda x: x[1], reverse=True)
        return sorted_scores[:num_scores]

    def draw_top_scores(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.title, (self.width / 3, self.height / 4))
        top = self.get_top_scores(min(len(self.scores), 5))
        for i in range(1, len(top) + 1):
            pygame.draw.rect(self.screen, RED, self.positions['position_%s' % i])
            (name, score) = top[i - 1]
            position_text = self.font.render(str(name) + ': ' + str(score), True, BLACK)
            self.screen.blit(position_text, (self.width / 3, self.height / 2 + self.height * i / 5))
        pygame.draw.rect(self.screen, RED, self.main_menu)
        main_menu_text = self.font.render('Back', True, BLACK)
        self.screen.blit(main_menu_text, (self.width / 10 + self.delta, self.height / 10 + self.delta / 5))
        pygame.display.update()
