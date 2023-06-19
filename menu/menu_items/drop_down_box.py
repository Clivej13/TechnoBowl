import pygame
from logger import Logger
from menu.menu_items.button import Button
from menu.menu_items.menu_item import MenuItem


class DropDownBox(MenuItem):
    def __init__(self, rect, data, font, menu_name):
        super().__init__()
        self.logger = Logger()
        self.menu_name = menu_name
        self.rect = rect
        self.data = data
        self.font = font
        self.color = (255, 255, 255)
        self.hover_color = (200, 200, 200)
        self.clicked_color = (100, 100, 100)
        self.active = False
        self.selected = False
        self.incorrect = False
        self.dropdown_open = False
        self.expandable = True
        self.menu_items_list = []
        for i, item in enumerate(self.data["list_items"]):
            item_rect = pygame.Rect(self.rect.x, self.rect.bottom + i * 30, self.rect.width, 30)
            button = Button(item_rect, item, self.font, self.data["menu_item_data"])
            self.menu_items_list.append(button)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)

        # Draw the drop-down box text
        text_surface = self.font.render(self.data["menu_item_value"], True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = self.rect.x + 10
        text_rect.centery = self.rect.centery
        surface.blit(text_surface, text_rect)

        # Draw the resolution text to the right of the text_rect
        resolution_text_surface = self.font.render(self.data["menu_item_data"], True, (0, 0, 0))
        resolution_text_rect = resolution_text_surface.get_rect()
        resolution_text_rect.x = text_rect.right + 10
        resolution_text_rect.centery = text_rect.centery
        surface.blit(resolution_text_surface, resolution_text_rect)

        if self.dropdown_open:
            dropdown_rect = pygame.Rect(self.rect.x, self.rect.bottom, self.rect.width, len(self.data["list_items"]) * 30)
            pygame.draw.rect(surface, (255, 255, 255), dropdown_rect)

            for item in self.menu_items_list:
                item.draw(surface)

    def handle_event(self, event):
        self.on_click()
        for menu_item in self.menu_items_list:
            if menu_item.rect.collidepoint(pygame.mouse.get_pos()):
                self.active = False
                self.data["menu_item_value"] = menu_item.handle_event(event)[0]["menu_item_data"]
                return menu_item.handle_event(event)

    def on_click(self):
        if self.dropdown_open:
            self.dropdown_open = False
        else:
            self.dropdown_open = True

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = self.hover_color
        else:
            self.color = (255, 255, 255)
        for item in self.menu_items_list:
            if item.rect.collidepoint(pygame.mouse.get_pos()):
                item.color = item.hover_color
            else:
                item.color = (255, 255, 255)

    def deselect(self):
        self.logger.log(self.dropdown_open)
        self.dropdown_open = False
