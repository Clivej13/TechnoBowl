import sys

import pygame

from menu.create_team_menu import CreateTeamMenu
from menu.menu import Menu
from menu.new_game_menu import NewGameMenu
from save import SaveGame


class OptionsMenu(Menu):
    # ...

    def check_state_transition(self):
        self.logger.log(str(self.current_state_output))
        if self.current_state_output is not None:
            SaveGame('temp/options_menu.json').save(SaveGame(self.json).load_all())
            if self.current_state_output[0]['menu_item_data'] == "Main Menu":
                from menu.main_menu import MainMenu
                return MainMenu(self.screen, self.background_image, 'menu/menu_jsons/main_menu.json')
            elif self.current_state_output[1] == "Resolution":
                self.logger.log(str(self.current_state_output))
                # apply change to resolution.
                resolution = self.current_state_output[0]["menu_item_data"].split("x")
                self.logger.log(str(resolution[0]) + " x " + str(resolution[1]))
                pygame.display.set_mode((int(resolution[0]), int(resolution[1])), pygame.FULLSCREEN)
                self.screen.fill((255, 255, 255))
                self.clear_screen()
                self.calculate_menu()
                apply = True
                if apply:
                    for menu_item in self.data["menu_items"]:
                        if menu_item["menu_item_data"] == "Resolution":
                            menu_temp = SaveGame('temp/options_menu.json').load_all()
                            menu_temp_menu_items = menu_temp["menu_items"]
                            for menu_item_temp in menu_temp_menu_items:
                                if menu_item_temp["menu_item_data"] == "Resolution":
                                    if menu_item_temp["menu_item_value"] != menu_item["menu_item_value"]:
                                        menu_item_temp["menu_item_value"] = menu_item["menu_item_value"]
                                        SaveGame('saved_data/options_menu.json').save(menu_temp)
