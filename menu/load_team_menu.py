import sys

import pygame

from menu.create_team_menu import CreateTeamMenu
from menu.delete_team_menu import DeleteTeamMenu
from menu.menu import Menu
from save import SaveGame


class LoadTeamMenu(Menu):
    # ...

    def check_state_transition(self):
        if self.current_state_output is not None:
            if self.current_state_output[0]['menu_item_data'] != "Done" and self.current_state_output[1] == "Load Team Menu":
                delete_team_menu = SaveGame('menu/menu_jsons/delete_team_menu.json').load_all()
                for menu_item in delete_team_menu["menu_items"]:
                    menu_item["id"] = self.current_state_output[0]["id"]
                SaveGame('temp/delete_team_menu.json').save(delete_team_menu)
                delete_team = DeleteTeamMenu(self.screen, self.background_image, 'temp/delete_team_menu.json')
                return delete_team
            elif self.current_state_output[0]['menu_item_data'] == "Done" and self.current_state_output[1] == "Load Team Menu":
                create_team_menu = CreateTeamMenu(self.screen, self.background_image, "menu/menu_jsons/create_team_menu.json")
                return create_team_menu
