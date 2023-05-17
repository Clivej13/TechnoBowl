import pygame

from logger import Logger
from menu.menu import Menu
from save import SaveGame


class CreateMenu:
    @staticmethod
    def create_menu(screen, json, background_image):
        data = SaveGame(json)
        create_team = Menu(screen, background_image, data.load_all())
        return create_team
