import sys

import pygame

from game import Game
from menu.create_franchise_menu import CreateFranchiseMenu
from menu.menu import Menu


class NewGameMenu(Menu):
    # ...

    def check_state_transition(self):
        if self.current_state_output is not None:
            if self.current_state_output[0]['menu_item_data'] == "Main Menu":
                from menu.main_menu import MainMenu
                return MainMenu(self.screen, self.background_image, 'menu/menu_jsons/main_menu.json')
            elif self.current_state_output[0]['menu_item_data'] == "Franchise" and self.current_state_output[1] == "New Game":
                return CreateFranchiseMenu(self.screen, self.background_image, "menu/menu_jsons/create_franchise_menu.json")
            elif self.current_state_output[0]['menu_item_data'] == "Quick Game" and self.current_state_output[1] == "New Game":
                return Game(self.screen, self.background_image)
