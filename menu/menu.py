import pygame

from menu.menu_items.button import Button
from menu.menu_items.input_box import InputBox
from logger import Logger
from menu.menu_items.display_box import DisplayBox
from menu.menu_items.toggle_box import ToggleBox
from save import SaveGame


class Menu:
    def __init__(self, screen, background_image, json):
        self.screen = screen
        self.background_image = background_image
        self.data = SaveGame(json).load_all()
        self.font = pygame.font.SysFont(None, 50)
        self.menu_items_list = []
        self.logger = Logger()
        self.current_state_output = None

        menu_item_spacing = 20
        menu_item_width = 200
        menu_item_height = 50
        self.menu_surface_height = 0

        for menu_item_data in self.data["menu_items"]:
            if "width" in menu_item_data:
                menu_item_width = max(menu_item_width, menu_item_data["width"])
            else:
                text_width, text_height = self.font.size(menu_item_data["menu_item_data"])
                menu_item_width = max(menu_item_width, text_width + (menu_item_spacing * 2))

        menu_item_width += menu_item_spacing

        for menu_item_data in self.data["menu_items"]:
            if "height" in menu_item_data:
                self.menu_surface_height += menu_item_data["height"] + menu_item_spacing
            else:
                self.menu_surface_height += menu_item_height + menu_item_spacing

        previous_menu_item_rect_y = screen.get_rect().center[1] - (self.menu_surface_height / 2) - (
                menu_item_spacing * 3)

        for i, menu_item_data in enumerate(self.data["menu_items"]):
            if "height" in menu_item_data:
                menu_item_rect = pygame.Rect(0, 0, menu_item_width, menu_item_data["height"])
                menu_item_height = menu_item_data["height"]
            else:
                menu_item_height = 50
                menu_item_rect = pygame.Rect(0, 0, menu_item_width, menu_item_height)

            menu_item_rect.center = screen.get_rect().center
            menu_item_rect.y = (previous_menu_item_rect_y + menu_item_height + menu_item_spacing)
            previous_menu_item_rect_y = menu_item_rect.y
            menu_item_data["menu_item_rect"] = menu_item_rect

        for menu_item_data in self.data["menu_items"]:
            menu_item_rect = menu_item_data["menu_item_rect"]
            if menu_item_data["menu_item_type"] == "Button":
                button = Button(menu_item_rect, menu_item_data, self.font, self.data["menu_name"])
                self.menu_items_list.append(button)
            if menu_item_data["menu_item_type"] == "Input Box":
                input_box = InputBox(menu_item_rect, menu_item_data, self.font, self.data["menu_name"])
                self.menu_items_list.append(input_box)
            if menu_item_data["menu_item_type"] == "Display Box":
                display_box = DisplayBox(menu_item_rect, menu_item_data, self.data["menu_name"])
                self.menu_items_list.append(display_box)
            if menu_item_data["menu_item_type"] == "Toggle Box":
                display_box = ToggleBox(menu_item_rect, menu_item_data, self.font, self.data["menu_name"])
                self.menu_items_list.append(display_box)

        self.menu_rect = pygame.Rect(0, 0, menu_item_width + menu_item_spacing, self.menu_surface_height)
        self.menu_rect.center = screen.get_rect().center
        self.menu_surface = pygame.Surface((self.menu_rect.width, self.menu_rect.height))
        self.menu_surface.set_alpha(200)
        self.menu_surface.fill((0, 0, 0))

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.menu_surface, self.menu_rect)
        for menu_item in self.menu_items_list:
            menu_item.draw(self.screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for menu_item in self.menu_items_list:
                if menu_item.rect.collidepoint(pygame.mouse.get_pos()):
                    for item in self.menu_items_list:
                        item.deselect()
                        item.incorrect_value()
                    button_clicked = menu_item.on_click()
                    self.current_state_output = button_clicked
        if event.type == pygame.KEYDOWN:
            for menu_item in self.menu_items_list:
                if menu_item.active:
                    if event.key == pygame.K_RETURN and menu_item.incorrect_value():
                        menu_item.deselect()
                    if event.key == pygame.K_BACKSPACE:
                        menu_item.data["menu_item_value"] = menu_item.data["menu_item_value"][:-1]
                    else:
                        menu_item.data["menu_item_value"] += event.unicode
                    menu_item.txt_surface = self.font.render(menu_item.data["menu_item_value"], True, menu_item.color)

    def update(self):
        for menu_item in self.menu_items_list:
            menu_item.update()
