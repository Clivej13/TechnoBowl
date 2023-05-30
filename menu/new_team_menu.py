import sys
from datetime import datetime

import pygame

from menu.create_team_menu import CreateTeamMenu
from menu.menu import Menu
from save import SaveGame


class NewTeamMenu(Menu):
    # ...

    def check_state_transition(self):
        if self.current_state_output is not None:
            if self.current_state_output[0]['menu_item_data'] == "Done" and self.current_state_output[1] == "New Team":
                return CreateTeamMenu(self.screen, self.background_image, "menu/menu_jsons/create_team_menu.json")
            elif self.current_state_output[0]['menu_item_data'] == "Save" and self.current_state_output[1] == "New Team":
                created_teams_data = SaveGame('saved_data/created_teams_data.json')
                data = {
                    "menu_item_data": self.menu_items_list[0].data["menu_item_value"],
                    "menu_item_type": "Button",
                    "menu_item_validation": "Text",
                    "id": datetime.now().strftime("%Y%m%d%H%M%S"),
                    "Team Name": self.menu_items_list[0].data["menu_item_value"],
                    "Location": self.menu_items_list[1].data["menu_item_value"],
                    "Primary_Color": self.menu_items_list[2].data["menu_item_value"],
                    "Secondary_Color": self.menu_items_list[3].data["menu_item_value"]
                }
                created_teams_data.append_item_to_list(data)
                return CreateTeamMenu(self.screen, self.background_image, "menu/menu_jsons/create_team_menu.json")
