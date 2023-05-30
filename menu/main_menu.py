import sys

import pygame

from menu.create_team_menu import CreateTeamMenu
from menu.menu import Menu


class MainMenu(Menu):
    # ...

    def check_state_transition(self):
        if self.current_state_output is not None:
            if self.current_state_output[0]['menu_item_data'] == "New Game" and self.current_state_output[1] == "Main Menu":
                new_game_menu = Menu(self.screen, self.background_image, "menu/menu_jsons/new_game_menu.json")
                return new_game_menu
            elif self.current_state_output[0]['menu_item_data'] == "Quit" and self.current_state_output[1] == "Main Menu":
                pygame.quit()
                sys.exit()
            elif self.current_state_output[0]['menu_item_data'] == "Create Team" and self.current_state_output[1] == "Main Menu":
                create_team_menu = CreateTeamMenu(self.screen, self.background_image, "menu/menu_jsons/create_team_menu.json")
                return create_team_menu
