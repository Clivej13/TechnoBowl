import pygame
import sys

from logger import Logger
from menu.main_menu import MainMenu


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
