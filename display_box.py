import pygame

from logger import Logger
from sprite import Sprite


class DisplayBox:
    def __init__(self, rect, text, font, menu_name):
        self.logger = Logger()
        self.menu_name = menu_name
        self.font = font
        self.rect = rect
        self.text = text
        self.active = False
        self.color = (255, 255, 255)
        self.sprite = Sprite(self.rect.x + (self.rect.w / 4), self.rect.y, self.text[2], self.text[3], self.text[4], 4,
                             False, 6, False)
        self.sprite.scale(self.text[5])

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.sprite.draw(surface)

    def on_click(self):
        pass

    def update(self):
        pass

    def deselect(self):
        pass
