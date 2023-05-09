import datetime
import pygame
import sys

from game import Game
from logger import Logger
from menu import Menu
from save import SaveGame


def main(self=None):
    logger = Logger()
    # initialize pygame
    pygame.init()

    # create a screen
    # screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("My Game")

    # load background image
    background_image = pygame.image.load("images/background.png").convert()
    created_teams_data = SaveGame('saved_data/created_teams_data.json')
    create_a_team_menu_data = SaveGame('menu/menu_jsons/new_team.json')
    create_team_menu_data = SaveGame('menu/menu_jsons/create_team_menu.json')
    load_team_data = SaveGame('load_team_menu')
    delete_team_menu_data = SaveGame('menu/menu_jsons/delete_team_menu.json')
    main_menu_data = SaveGame('menu/menu_jsons/main_menu.json')
    pause_menu_data = SaveGame('menu/menu_jsons/pause_menu.json')

    # main game loop
    # create instances of the menu and game classes
    main_menu = Menu(screen, background_image, main_menu_data.load_all())
    pause_menu = Menu(screen, background_image, pause_menu_data.load_all())
    create_team_menu = Menu(screen, background_image, create_team_menu_data.load_all())
    create_team = Menu(screen, background_image, create_a_team_menu_data.load_all())

    current_state = main_menu  # start with the main menu

    # main game loop
    while True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            current_state_output = current_state.handle_event(event)
            if current_state_output is not None:
                if current_state_output[0] == "Main Menu" and current_state_output[1] == "Pause Menu":
                    current_state = main_menu
                elif current_state_output[0] == "New Game" and current_state_output[1] == "Main Menu":
                    game = Game(screen, background_image)
                    current_state = game
                elif current_state_output[0] == "Quit" and current_state_output[1] == "Main Menu":
                    pygame.quit()
                    sys.exit()
                elif current_state_output == "Pause":
                    current_state = pause_menu
                elif current_state_output[0] == "Resume Game" and current_state_output[1] == "Pause Menu":
                    current_state = game
                elif current_state_output[0] == "Create Team" and current_state_output[1] == "Main Menu":
                    current_state = create_team_menu
                elif current_state_output[0] == "Main Menu" and current_state_output[1] == "Create Team":
                    current_state = main_menu
                elif current_state_output[0] == "New Team" and current_state_output[1] == "Create Team":
                    current_state = create_team
                elif current_state_output[0] == "Load Team" and current_state_output[1] == "Create Team":
                    load_team_menu = load_team_data.load_all()
                    teams = created_teams_data.load_all()
                    for team in teams:
                        load_team_menu["menu_items"].append(
                            {"menu_item_data": team["Team Name"], "menu_item_type": "button", "id": team["id"]})
                    load_team = Menu(screen, background_image, load_team_menu)
                    current_state = load_team
                elif current_state_output[0] != "Done" and current_state_output[1] == "Load Team":
                    delete_team_menu = delete_team_menu_data.load_all()
                    delete_team_menu.append({"id": current_state_output[0][3]})
                    delete_team = Menu(screen, background_image, delete_team_menu)
                    current_state = delete_team
                elif current_state_output[0] == "Done" and current_state_output[1] == "Delete Team":
                    current_state = load_team
                elif current_state_output[0] == "Delete" and current_state_output[1] == "Delete Team":
                    created_teams_data.delete_item_from_list(current_state_output[3])
                    current_state = create_team_menu
                elif current_state_output[0] == "Load" and current_state_output[1] == "Delete Team":
                    data = created_teams_data.load_item_from_list(current_state_output[3])
                    logger.log(str(data))
                    create_team_data = create_a_team_menu_data.load_all()
                    for menu_item in create_team_data["menu_items"]:
                        if menu_item["menu_item_data"] == "Team Name":
                            menu_item["menu_item_value"] = data["Team Name"]
                        if menu_item["menu_item_data"] == "Team Location":
                            menu_item["menu_item_value"] = data["Location"]
                        if menu_item["menu_item_data"] == "Primary Color":
                            menu_item["menu_item_value"] = data["Primary_Color"]
                        if menu_item["menu_item_data"] == "Secondary Color":
                            menu_item["menu_item_value"] == data["Secondary_Color"]
                    create_team = Menu(screen, background_image, create_team_data)
                    #created_teams_data.delete_item_from_list(current_state_output[0][3])
                    current_state = create_team
                elif current_state_output[0] == "Done" and current_state_output[1] == "Load Team":
                    current_state = main_menu
                elif current_state_output[0] == "Done" and current_state_output[1] == "New Team":
                    current_state = create_team_menu
                elif current_state_output[0] == "Save" and current_state_output[1] == "New Team":
                    data = {
                        "id": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
                        "Team Name": create_team.menu_items[0].data[0],
                        "Location": create_team.menu_items[1].data[0],
                        "Primary_Color": create_team.menu_items[2].data[0],
                        "Secondary_Color": create_team.menu_items[3].data[0]
                    }
                    created_teams_data.append_item_to_list(data)

        current_state.update()
        current_state.draw()

        # update the display
        pygame.display.update()


if __name__ == "__main__":
    main()
