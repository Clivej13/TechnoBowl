import pygame
from logger import Logger


class ToggleBox:
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
        self.selected = False
        self.incorrect = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        toggle_circle_radius = 12
        toggle_circle_x = self.rect.x + toggle_circle_radius + 5
        toggle_circle_y = self.rect.centery
        pygame.draw.circle(surface, (255, 255, 255), (toggle_circle_x, toggle_circle_y), toggle_circle_radius)
        if self.selected:
            pygame.draw.circle(surface, (0, 255, 0), (toggle_circle_x, toggle_circle_y), toggle_circle_radius - 4)

        text_surface = self.font.render(self.data["menu_item_data"], True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = toggle_circle_x + toggle_circle_radius + 10
        text_rect.centery = self.rect.centery
        surface.blit(text_surface, text_rect)

    def on_click(self):
        if self.selected:
            self.selected = False
            self.data["menu_item_value"] = "No"
        elif not self.selected:
            self.selected = True
            self.data["menu_item_value"] = "Yes"

        return [self.data, self.menu_name]

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = self.hover_color
        else:
            self.color = (255, 255, 255)

    def deselect(self):
        pass
