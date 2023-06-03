import sys

import pygame

from game import Game
from menu.menu import Menu


class CreateFranchiseMenu(Menu):
    # ...

    def check_state_transition(self):
        if self.current_state_output is not None:
            if self.current_state_output[0]['menu_item_data'] == "Main Menu":
                from menu.main_menu import MainMenu
                return MainMenu(self.screen, self.background_image, 'menu/menu_jsons/main_menu.json')
