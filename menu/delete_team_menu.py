import sys

import pygame

import logger
from menu.create_team_menu import CreateTeamMenu
from menu.menu import Menu
from menu.new_team_menu import NewTeamMenu
from save import SaveGame


class DeleteTeamMenu(Menu):
    # ...

    def check_state_transition(self):
        if self.current_state_output is not None:
            if self.current_state_output[0]['menu_item_data'] == "Done" and self.current_state_output[1] == "Delete Team Menu":
                load_team_menu = SaveGame('menu/menu_jsons/load_team_menu.json').load_all()
                created_teams_data = SaveGame('saved_data/created_teams_data.json').load_all()
                for team in created_teams_data:
                    load_team_menu["menu_items"].append(team)
                SaveGame('temp/load_team_menu.json').save(load_team_menu)
                from menu.load_team_menu import LoadTeamMenu
                return LoadTeamMenu(self.screen, self.background_image, 'temp/load_team_menu.json')
            elif self.current_state_output[0]['menu_item_data'] == "Delete" and self.current_state_output[1] == "Delete Team Menu":
                SaveGame('saved_data/created_teams_data.json').delete_item_from_list(self.current_state_output[0]["id"])
                create_team_menu = CreateTeamMenu(self.screen, self.background_image, "menu/menu_jsons/create_team_menu.json")
                return create_team_menu
            elif self.current_state_output[0]['menu_item_data'] == "Load" and self.current_state_output[1] == "Delete Team Menu":
                data = SaveGame('saved_data/created_teams_data.json').load_item_from_list(self.current_state_output[0]["id"])
                create_team_data = SaveGame('menu/menu_jsons/new_team_menu.json').load_all()
                for menu_item in create_team_data["menu_items"]:
                    if menu_item["menu_item_data"] == "Team Name":
                        menu_item["menu_item_value"] = data["Team Name"]
                    if menu_item["menu_item_data"] == "Team Location":
                        menu_item["menu_item_value"] = data["Location"]
                    if menu_item["menu_item_data"] == "Primary Color":
                        menu_item["menu_item_value"] = data["Primary_Color"]
                    if menu_item["menu_item_data"] == "Secondary Color":
                        menu_item["menu_item_value"] = data["Secondary_Color"]
                create_team_data["loaded"] = True
                create_team_data["id"] = self.current_state_output[0]["id"]
                SaveGame('temp/new_team_menu.json').save(create_team_data)
                return NewTeamMenu(self.screen, self.background_image, "temp/new_team_menu.json")
