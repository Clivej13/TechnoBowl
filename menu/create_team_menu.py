import sys

import pygame

from menu.menu import Menu
from save import SaveGame


class CreateTeamMenu(Menu):
    # ...

    def check_state_transition(self):
        from menu.main_menu import MainMenu
        if self.current_state_output is not None:
            if self.current_state_output[0]['menu_item_data'] == "Main Menu":
                return MainMenu(self.screen, self.background_image, 'menu/menu_jsons/main_menu.json')
            elif self.current_state_output[0]['menu_item_data'] == "New Team" and self.current_state_output[1] == "Create Team":
                from menu.new_team_menu import NewTeamMenu
                return NewTeamMenu(self.screen, self.background_image, "menu/menu_jsons/new_team_menu.json")
            elif self.current_state_output[0]['menu_item_data'] == "Load Team" and self.current_state_output[1] == "Create Team":
                load_team_menu = SaveGame('menu/menu_jsons/load_team_menu.json').load_all()
                created_teams_data = SaveGame('saved_data/created_teams_data.json').load_all()
                for team in created_teams_data:
                    load_team_menu["menu_items"].append(team)
                SaveGame('temp/load_team_menu.json').save(load_team_menu)
                from menu.load_team_menu import LoadTeamMenu
                return LoadTeamMenu(self.screen, self.background_image, 'temp/load_team_menu.json')
