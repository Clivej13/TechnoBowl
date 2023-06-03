import sys

import pygame

from menu.create_team_menu import CreateTeamMenu
from menu.menu import Menu
from menu.new_game_menu import NewGameMenu


class OptionsMenu(Menu):
    # ...

    def check_state_transition(self):
        if self.current_state_output is not None:
            if self.current_state_output[0]['menu_item_data'] == "New Game" and self.current_state_output[1] == "Main Menu":
                return NewGameMenu(self.screen, self.background_image, "menu/menu_jsons/new_game_menu.json")
            elif self.current_state_output[0]['menu_item_data'] == "Main Menu":
                from menu.main_menu import MainMenu
                return MainMenu(self.screen, self.background_image, 'menu/menu_jsons/main_menu.json')
