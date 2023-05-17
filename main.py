import datetime
import pygame
import sys

from game import Game
from logger import Logger
from menu.menu import Menu
from save import SaveGame
from menu.create_menu import CreateMenu


def main(self=None):
    logger = Logger()
    # initialize pygame
    pygame.init()

    # create a screen
    # screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1280, 720))
    # screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("My Game")

    # load background image
    background_image = pygame.image.load("images/background.png").convert()
    new_team_menu_data = SaveGame('menu/menu_jsons/new_team.json')
    load_team_data = SaveGame('menu/menu_jsons/load_team_menu.json')
    delete_team_menu_data = SaveGame('menu/menu_jsons/delete_team_menu.json')

    main_menu = CreateMenu.create_menu(screen, 'menu/menu_jsons/main_menu.json', background_image)
    new_game_menu = CreateMenu.create_menu(screen, "menu/menu_jsons/new_game_menu.json", background_image)
    create_team_menu = CreateMenu.create_menu(screen, "menu/menu_jsons/create_team_menu.json", background_image)
    new_team_menu = CreateMenu.create_menu(screen, "menu/menu_jsons/new_team.json", background_image)
    pause_menu = CreateMenu.create_menu(screen, "menu/menu_jsons/pause_menu.json", background_image)

    current_state = main_menu  # start with the main menu
    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            current_state_output = current_state.handle_event(event)
            if current_state_output is not None:
                if current_state_output[0]['menu_item_data'] == "Main Menu":
                    current_state = main_menu
                elif current_state_output[0]['menu_item_data'] == "New Game" and current_state_output[1] == "Main Menu":
                    current_state = new_game_menu
                elif current_state_output[0]['menu_item_data'] == "Franchise" and current_state_output[1] == "New Game":
                    create_franchise_menu = CreateMenu.create_menu(screen, "menu/menu_jsons/create_franchise_menu.json", background_image)
                    current_state = create_franchise_menu
                elif current_state_output[0]['menu_item_data'] == "Quick Game" and current_state_output[1] == "New Game":
                    game = Game(screen, background_image)
                    current_state = game
                elif current_state_output[0]['menu_item_data'] == "Quit" and current_state_output[1] == "Main Menu":
                    pygame.quit()
                    sys.exit()
                elif current_state_output[0]['menu_item_data'] == "Pause":
                    current_state = pause_menu
                elif current_state_output[0]['menu_item_data'] == "Resume Game" and current_state_output[1] == "Pause Menu":
                    current_state = game
                elif current_state_output[0]['menu_item_data'] == "Create Team" and current_state_output[1] == "Main Menu":
                    current_state = create_team_menu
                elif current_state_output[0]['menu_item_data'] == "New Team" and current_state_output[1] == "Create Team":
                    current_state = new_team_menu
                    loaded = False
                elif current_state_output[0]['menu_item_data'] == "Load Team" and current_state_output[1] == "Create Team":
                    load_team_menu = load_team_data.load_all()
                    created_teams_data = SaveGame('saved_data/created_teams_data.json')
                    teams = created_teams_data.load_all()
                    for team in teams:
                        load_team_menu["menu_items"].append(team)
                    load_team = Menu(screen, background_image, load_team_menu)
                    current_state = load_team
                elif current_state_output[0]['menu_item_data'] != "Done" and current_state_output[1] == "Load Team Menu":
                    delete_team_menu = delete_team_menu_data.load_all()
                    for menu_item in delete_team_menu["menu_items"]:
                        menu_item["id"] = current_state_output[0]["id"]
                    delete_team = Menu(screen, background_image, delete_team_menu)
                    current_state = delete_team
                elif current_state_output[0]['menu_item_data'] == "Done" and current_state_output[1] == "Load Team Menu":
                    current_state = create_team_menu
                elif current_state_output[0]['menu_item_data'] == "Done" and current_state_output[1] == "Delete Team Menu":
                    current_state = load_team
                elif current_state_output[0]['menu_item_data'] == "Delete" and current_state_output[1] == "Delete Team Menu":
                    created_teams_data = SaveGame('saved_data/created_teams_data.json')
                    created_teams_data.delete_item_from_list(current_state_output[0]["id"])
                    current_state = create_team_menu
                elif current_state_output[0]['menu_item_data'] == "Load" and current_state_output[1] == "Delete Team Menu":
                    created_teams_data = SaveGame('saved_data/created_teams_data.json')
                    loaded = True
                    data = created_teams_data.load_item_from_list(current_state_output[0]["id"])
                    logger.log(data)
                    create_team_data = new_team_menu_data.load_all()
                    for menu_item in create_team_data["menu_items"]:
                        if menu_item["menu_item_data"] == "Team Name":
                            menu_item["menu_item_value"] = data["Team Name"]
                        if menu_item["menu_item_data"] == "Team Location":
                            menu_item["menu_item_value"] = data["Location"]
                        if menu_item["menu_item_data"] == "Primary Color":
                            menu_item["menu_item_value"] = data["Primary_Color"]
                        if menu_item["menu_item_data"] == "Secondary Color":
                            menu_item["menu_item_value"] = data["Secondary_Color"]
                    new_team = Menu(screen, background_image, create_team_data)
                    current_state = new_team
                elif current_state_output[0]['menu_item_data'] == "Done" and current_state_output[1] == "Load Team":
                    current_state = main_menu
                elif current_state_output[0]['menu_item_data'] == "Done" and current_state_output[1] == "New Team":
                    current_state = create_team_menu
                elif current_state_output[0]['menu_item_data'] == "Save" and current_state_output[1] == "New Team":
                    if loaded:
                        pass
                    else:
                        created_teams_data = SaveGame('saved_data/created_teams_data.json')
                        logger.log(new_team_menu.menu_items_list)
                        data = {
                            "menu_item_data": new_team_menu.menu_items_list[0].data["menu_item_value"],
                            "menu_item_type": "Button",
                            "menu_item_validation": "Text",
                            "id": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
                            "Team Name": new_team_menu.menu_items_list[0].data["menu_item_value"],
                            "Location": new_team_menu.menu_items_list[1].data["menu_item_value"],
                            "Primary_Color": new_team_menu.menu_items_list[2].data["menu_item_value"],
                            "Secondary_Color": new_team_menu.menu_items_list[3].data["menu_item_value"]
                        }
                        created_teams_data.append_item_to_list(data)
                        current_state = create_team_menu

        current_state.update()
        current_state.draw()

        # update the display
        pygame.display.update()


if __name__ == "__main__":
    main()
