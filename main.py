import pygame
import sys

from logger import Logger
from menu.main_menu import MainMenu
from save import SaveGame


def main(self=None):
    logger = Logger()
    # initialize pygame
    pygame.init()

    # create a screen
    try:
        options = SaveGame('saved_data/options_menu.json').load_all()
    except:
        options = SaveGame('menu/menu_jsons/options_menu.json').load_all()
    logger.log(str(options))
    for menu_item in options["menu_items"]:
        if menu_item["menu_item_data"] == "Resolution":
            resolution = menu_item["menu_item_value"].split("x")
            # screen = pygame.display.set_mode((int(resolution[0]), int(resolution[1])))
            screen = pygame.display.set_mode((int(resolution[0]), int(resolution[1])), pygame.FULLSCREEN)
    pygame.display.set_caption("My Game")

    # load background image
    background_image = pygame.image.load("images/background.png").convert()
    main_menu = MainMenu(screen, background_image, 'menu/menu_jsons/main_menu.json')
    current_state = main_menu  # start with the main menu
    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            current_state.handle_event(event)
        next_state = current_state.check_state_transition()
        if next_state is not None:
            current_state = next_state
        current_state.update()
        current_state.draw()

        # update the display
        pygame.display.update()


if __name__ == "__main__":
    main()
