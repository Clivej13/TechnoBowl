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
    save_game = SaveGame('my_game.json')

    # main game loop
    # create instances of the menu and game classes
    main_menu = Menu(screen, background_image,
                     [["New Game", "button", "Text"], ["Load Game", "button", "Text"], ["Options", "button", "Text"],
                      ["Create Team", "button", "Text"],
                      ["Quit", "button", "Text"]], "Main Menu")
    pause_menu = Menu(screen, background_image,
                      [["Resume Game", "button", "Text"], ["Save Game", "button", "Text"],
                       ["Main Menu", "button", "Text"]], "Pause")
    create_team_menu = Menu(screen, background_image,
                            [["New Team", "button", "Text"], ["Load Team", "button", "Text"],
                             ["Main Menu", "button", "Text"]],
                            "Create Team")
    create_team = Menu(screen, background_image,
                       [["Team Name", "input box", "Text"], ["Team Location", "input box", "Text"],
                        ["Primary Color", "input box", "Color"],
                        ["Secondary Color", "input box", "Color"],
                        ["Save", "button", "Text"],
                        ["Done", "button", "Text"],
                        ["Test", "display box", "images/footballer_new.png", 66, 66, 3]],
                       "New Team")

    current_state = create_team  # start with the main menu

    # main game loop
    while True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            current_state_output = current_state.handle_event(event)
            if current_state_output is not None:
                if current_state_output[0][0] == "Main Menu" and current_state_output[1] == "Pause":
                    current_state = main_menu
                elif current_state_output[0][0] == "New Game" and current_state_output[1] == "Main Menu":
                    game = Game(screen, background_image)
                    current_state = game
                elif current_state_output[0][0] == "Quit" and current_state_output[1] == "Main Menu":
                    pygame.quit()
                    sys.exit()
                elif current_state_output == "Pause":
                    current_state = pause_menu
                elif current_state_output[0][0] == "Resume Game" and current_state_output[1] == "Pause":
                    current_state = game
                elif current_state_output[0][0] == "Create Team" and current_state_output[1] == "Main Menu":
                    current_state = create_team_menu
                elif current_state_output[0][0] == "Main Menu" and current_state_output[1] == "Create Team":
                    current_state = main_menu
                elif current_state_output[0][0] == "New Team" and current_state_output[1] == "Create Team":
                    create_team = Menu(screen, background_image,
                                       [["Team Name", "input box", "Text"], ["Team Location", "input box", "Text"],
                                        ["Primary Color", "input box", "Color"],
                                        ["Secondary Color", "input box", "Color"],
                                        ["Save", "button", "Text"],
                                        ["Done", "button", "Text"],
                                        ["Test", "display box", "images/footballer_new.png", 66, 66, 3]],
                                       "New Team")
                    current_state = create_team
                elif current_state_output[0][0] == "Load Team" and current_state_output[1] == "Create Team":
                    menu_items = [["Done", "button", "Text"]]
                    teams = save_game.load_all("Teams")
                    for team in teams:
                        menu_items.append([team["Team Name"], "button", "text", team["id"]])
                    load_team = Menu(screen, background_image,
                                     menu_items,
                                     "Load Team")
                    current_state = load_team
                elif current_state_output[0][0] != "Done" and current_state_output[1] == "Load Team":
                    delete_team = Menu(screen, background_image,
                                       [["Load", "button", "Text", current_state_output[0][3]],
                                        ["Delete", "button", "Text", current_state_output[0][3]],
                                        ["Done", "button", "Text"]],
                                       "Delete Team")
                    current_state = delete_team
                elif current_state_output[0][0] == "Done" and current_state_output[1] == "Delete Team":
                    current_state = load_team
                elif current_state_output[0][0] == "Delete" and current_state_output[1] == "Delete Team":
                    save_game.delete(current_state_output[0][3], "Teams")
                    current_state = create_team_menu
                elif current_state_output[0][0] == "Load" and current_state_output[1] == "Delete Team":
                    data = save_game.load(current_state_output[0][3], "Teams")
                    logger.log(str(data))
                    create_team = Menu(screen, background_image,
                                       [[data["Team Name"], "input box", "Text"],
                                        [data["Location"], "input box", "Text"],
                                        [data["Primary_Color"], "input box", "Color"],
                                        [data["Secondary_Color"], "input box", "Color"],
                                        ["Save", "button", "Text"],
                                        ["Done", "button", "Text"],
                                        ["Test", "display box", "images/footballer_new.png", 66, 66, 3]],
                                       "New Team")
                    save_game.delete(current_state_output[0][3], "Teams")
                    current_state = create_team
                elif current_state_output[0][0] == "Done" and current_state_output[1] == "Load Team":
                    current_state = main_menu
                elif current_state_output[0][0] == "Done" and current_state_output[1] == "New Team":
                    current_state = create_team_menu
                elif current_state_output[0][0] == "Save" and current_state_output[1] == "New Team":
                    data = {
                        "id": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
                        "Team Name": create_team.menu_items[0].text[0],
                        "Location": create_team.menu_items[1].text[0],
                        "Primary_Color": create_team.menu_items[2].text[0],
                        "Secondary_Color": create_team.menu_items[3].text[0]
                    }
                    save_game.append(data, "Teams")

        current_state.update()
        current_state.draw()

        # update the display
        pygame.display.update()


if __name__ == "__main__":
    main()
