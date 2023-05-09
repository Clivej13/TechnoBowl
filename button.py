import pygame

from logger import Logger


class Button:
    def __init__(self, rect, data, font, menu_name):
        self.logger = Logger()
        self.menu_name = menu_name
        self.rect = rect
        self.data = data
        self.font = font
        self.color = (255, 255, 255)
        self.hover_color = (200, 200, 200)
        self.clicked_color = (100, 100, 100)
        self.active = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.data["menu_item_data"], True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        surface.blit(text_surface, text_rect)

    def on_click(self):
        self.logger.log("Clicked button: " + str(self.data["menu_item_data"]) + " on " + self.menu_name)
        return [self.data["menu_item_data"], self.menu_name]

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = self.hover_color
        else:
            self.color = (255, 255, 255)

    def deselect(self):
        pass
