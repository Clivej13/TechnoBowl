import pygame

from logger import Logger
from sprite import Sprite


class DisplayBox:
    def __init__(self, rect, data, menu_name):
        self.logger = Logger()
        self.menu_name = menu_name
        self.rect = rect
        self.data = data
        self.active = False
        self.color = (255, 255, 255)
        x_buffer = (self.rect.width - self.data["frame_width"]) / 4
        self.rect.y -= rect.height - x_buffer
        self.sprite = Sprite(self.rect.x + x_buffer, self.rect.y, self.data["menu_item_data"], self.data["frame_width"],
                             self.data["frame_height"], self.data["number_of_frames"],
                             False, 6, False)
        self.sprite.scale(self.data["scale_factor"])
        self.incorrect = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.sprite.draw(surface)

    def on_click(self):
        pass

    def update(self):
        pass

    def deselect(self):
        pass

    def incorrect_value(self):
        pass
