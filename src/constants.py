WIDTH = 500
HEIGHT = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (175, 75, 0)

CELL_SIZE = 20

RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)


class InterfaceBack:
    def __init__(self, width, height):
        self.button_width = width / 10
        self.button_height = height / 10
        self.button_length = width / 5
        self.button_thickness = 30
        self.width_shift = 25
        self.height_shift = 5


class InterfaceMainMenu:
    def __init__(self, width, height):
        self.title_width = width / 2 - 70
        self.title_height = height / 4
        self.button_width = width / 3
        self.first_button_height = height / 3
        self.second_button_height = self.first_button_height * 3 / 2
        self.third_button_height = self.first_button_height * 2
        self.length_button = width * 3 / 8
        self.thickness = 60
        self.big_thickness = 85
        self.shift_height = 15
        self.start_shift_width = 65
        self.setting_shift_width = 45
        self.leader_shift_width = 50
        self.board_shift_width = 60
        self.board_shift_height = 3 * self.shift_height


class InterfaceEndMenu:
    def __init__(self, width, height):
        self.title_width = width / 3
        self.title_height = height / 4
        self.button_width = width / 3
        self.length_button = width / 3
        self.retry_height = height * 2 / 3
        self.menu_height = height * 3 / 4
        self.score_width = width / 3 + 20
        self.score_height = height / 2
        self.thickness = 30
        self.retry_width_shift = width // 10 + 10
        self.retry_height_shift = 5
        self.menu_width_shift = width // 12
        self.menu_height_shift = 5


class InterfaceSettingMenu:
    def __init__(self, width, height):
        self.title_width = width / 3 + 50
        self.title_height = height / 4
        self.length_level_width = width / 3
        self.length_level_height = 35
        self.level_width = width / 3
        self.first_button_height = height / 2 - 50
        self.between_buttons = self.length_level_height * 3 / 2
        self.text_width_shift = 50
        self.text_height_shift = 9


class InterfaceLeaderBoard:
    def __init__(self, width, height):
        self.title_width = width / 4
        self.title_height = height / 3
        self.length_player = width / 3
        self.width_player = width / 3
        self.thickness = 35
        self.first_player_height = height / 2 - 70
        self.between_players = self.thickness * 3 / 2
        self.text_width_shift = 55
        self.text_height_shift = 9
