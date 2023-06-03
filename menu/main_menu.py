import sys

import pygame

from menu.create_team_menu import CreateTeamMenu
from menu.menu import Menu
from menu.new_game_menu import NewGameMenu
from menu.options_menu import OptionsMenu


class MainMenu(Menu):
    # ...

    def check_state_transition(self):
        if self.current_state_output is not None:
            if self.current_state_output[0]['menu_item_data'] == "New Game" and self.current_state_output[1] == "Main Menu":
                return NewGameMenu(self.screen, self.background_image, "menu/menu_jsons/new_game_menu.json")
            elif self.current_state_output[0]['menu_item_data'] == "Quit" and self.current_state_output[1] == "Main Menu":
                pygame.quit()
                sys.exit()
            elif self.current_state_output[0]['menu_item_data'] == "Create Team" and self.current_state_output[1] == "Main Menu":
                return CreateTeamMenu(self.screen, self.background_image, "menu/menu_jsons/create_team_menu.json")
            elif self.current_state_output[0]['menu_item_data'] == "Options" and self.current_state_output[1] == "Main Menu":
                return OptionsMenu(self.screen, self.background_image, "menu/menu_jsons/options_menu.json")
