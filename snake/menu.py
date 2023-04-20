import pygame
from constants import *

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Arial', 30)
        self.title = self.font.render('Snake Game', True, BLACK)
        self.start_button = pygame.Rect(self.width/2-100, self.height/2-50, 200, 50)
        self.settings_button = pygame.Rect(self.width/2-100, self.height/2+50, 200, 50)

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.title, (self.width/2-70, self.height/4))
        pygame.draw.rect(self.screen, RED, self.start_button)
        pygame.draw.rect(self.screen, GREEN, self.settings_button)
        start_text = self.font.render('Start', True, BLACK)
        settings_text = self.font.render('Settings', True, BLACK)
        self.screen.blit(start_text, (self.width/2-30, self.height/2-40))
        self.screen.blit(settings_text, (self.width/2-45, self.height/2+60))
        pygame.display.update()

class EndMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Arial', 20)
        self.title = self.font.render('Wasted!', True, BLACK)
        self.retry = pygame.Rect(self.width/2, self.height/2, 100, 50)

    def draw(self, score):
        self.screen.fill(WHITE)
        self.screen.blit(self.title, (self.width/2, self.height/4))
        pygame.draw.rect(self.screen, RED, self.retry)
        retry_text = self.font.render('Retry', True, BLACK)
        score_text = self.font.render('Your score: ' + str(score), True, BLACK)
        self.screen.blit(retry_text, (self.width/2 + 30, self.height/2 + 10))
        self.screen.blit(score_text, (self.width/2, self.height/2-40))
        pygame.display.update()

class Setting:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Arial', 20)
        self.title = self.font.render('Settings', True, BLACK)
        self.first_level = pygame.Rect(self.width / 5, self.height * 2 / 3, 75, 75)
        self.second_level = pygame.Rect(self.width * 2 / 5 + 10, self.height * 2 / 3, 75, 75)
        self.third_level = pygame.Rect(self.width * 3 / 5 + 10, self.height * 2 / 3, 75, 75)
        self.fourth_level = pygame.Rect(self.width * 4 / 5, self.height* 2 / 3, 75, 75)

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.title, (self.width/2-70, self.height/4))
        pygame.draw.rect(self.screen, GREEN, self.first_level)
        pygame.draw.rect(self.screen, GREEN, self.second_level)
        pygame.draw.rect(self.screen, GREEN, self.third_level)
        pygame.draw.rect(self.screen, GREEN, self.fourth_level)
        first_level_text = self.font.render('1 level', True, BLACK)
        second_level_text = self.font.render('2 level', True, BLACK)
        third_level_text = self.font.render('3 level', True, BLACK)
        fourth_level_text = self.font.render('4 level', True, BLACK)
        self.screen.blit(first_level_text, (self.width / 5, self.height * 2 / 3))
        self.screen.blit(second_level_text, (self.width * 2 / 5, self.height * 2 / 3))
        self.screen.blit(third_level_text, (self.width * 3 / 5, self.height * 2 / 3))
        self.screen.blit(fourth_level_text, (self.width * 4 / 5, self.height * 2 / 3))
        pygame.display.update()

