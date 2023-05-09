import pygame

import logger
from button import Button
from input_box import InputBox
from logger import Logger
from display_box import DisplayBox


class Menu:
    def __init__(self, screen, background_image, data):
        self.screen = screen
        self.background_image = background_image
        self.data = data
        self.menu_surface = pygame.Surface((400, 400))
        self.menu_surface.set_alpha(200)
        self.menu_surface.fill((0, 0, 0))
        self.menu_rect = self.menu_surface.get_rect()
        self.font = pygame.font.SysFont(None, 50)
        menu_item_spacing = 20
        menu_item_height = 50
        menu_item_width = 200
        self.menu_items = []
        self.logger = Logger()

        for menu_item_data in self.data["menu_items"]:
            if "width" in menu_item_data:
                if menu_item_data["width"] > menu_item_width:
                    menu_item_width = menu_item_data["width"]

        for i, menu_item_data in enumerate(self.data["menu_items"]):
            menu_item_rect = pygame.Rect(0, 0, menu_item_width, menu_item_height)
            menu_item_rect.center = self.menu_rect.center
            menu_item_rect.y += (i * (menu_item_height + menu_item_spacing)) - (
                    ((menu_item_height + menu_item_spacing) * len(menu_item_data) - (
                            menu_item_height + menu_item_spacing)) / 2)
            if menu_item_data["menu_item_type"] == "Button":
                button = Button(menu_item_rect, menu_item_data, self.font, data["menu_name"])
                self.menu_items.append(button)
            if menu_item_data["menu_item_type"] == "Input Box":
                input_box = InputBox(menu_item_rect, menu_item_data, self.font, data["menu_name"])
                self.menu_items.append(input_box)
            if menu_item_data["menu_item_type"] == "Display Box":
                display_box = DisplayBox(menu_item_rect, menu_item_data, data["menu_name"])
                self.menu_items.append(display_box)

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.menu_surface, self.menu_rect)
        for menu_items in self.menu_items:
            menu_items.draw(self.screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for menu_item in self.menu_items:
                if menu_item.rect.collidepoint(pygame.mouse.get_pos()):
                    for each in self.menu_items:
                        each.deselect()
                    button_clicked = menu_item.on_click()
                    self.logger.log("Clicked button: " + str(button_clicked))
                    return button_clicked
                else:
                    menu_item.active = False
        if event.type == pygame.KEYDOWN:
            for menu_item in self.menu_items:
                if menu_item.active:
                    if event.key == pygame.K_RETURN and menu_item.incorrect_value():
                        print(menu_item.data[0])
                        menu_item.active = False
                    elif event.key == pygame.K_BACKSPACE:
                        menu_item.data[0] = menu_item.data[0][:-1]
                    else:
                        menu_item.data[0] += event.unicode
                    # Re-render the text.
                    menu_item.txt_surface = pygame.font.Font(None, 32).render(menu_item.data[0], True, menu_item.color)

        return None

    def update(self):
        for menu_items in self.menu_items:
            menu_items.update()
