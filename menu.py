import pygame

import logger
from button import Button
from input_box import InputBox
from logger import Logger
from display_box import DisplayBox


class Menu:
    def __init__(self, screen, background_image, button_texts, menu_name):
        self.logger = Logger()
        self.screen = screen
        self.background_image = background_image
        self.button_texts = button_texts
        self.menu_items = []

        self.font = pygame.font.SysFont(None, 50)

        self.menu_surface = pygame.Surface((400, 400))
        self.menu_surface.set_alpha(200)
        self.menu_surface.fill((0, 0, 0))

        self.menu_rect = self.menu_surface.get_rect()
        self.menu_rect.center = screen.get_rect().center
        self.menu_item_spacing = 20
        self.menu_item_width = 200
        self.menu_item_height = 50
        for text in self.button_texts:
            text_width, text_height = self.font.size(text[0])
            if text[1] == "display box":
                text_width = text[3] * text[5]
                if int(text_width) > self.menu_item_width:
                    self.menu_item_width = int(text_width) + (self.menu_item_spacing * 2)
            elif int(text_width) > self.menu_item_width:
                self.menu_item_width = int(text_width) + (self.menu_item_spacing * 2)

        self.menu_surface = pygame.Surface((self.menu_item_width + self.menu_item_spacing,
                                            (self.menu_item_height + self.menu_item_spacing) * len(self.button_texts)))
        self.menu_surface.set_alpha(200)
        self.menu_surface.fill((0, 0, 0))

        self.menu_rect = self.menu_surface.get_rect()
        self.menu_rect.center = screen.get_rect().center
        for i, text in enumerate(self.button_texts):
            menu_item_rect = pygame.Rect(0, 0, self.menu_item_width, self.menu_item_height)
            menu_item_rect.center = self.menu_rect.center
            menu_item_rect.y += (i * (self.menu_item_height + self.menu_item_spacing)) - (
                    ((self.menu_item_height + self.menu_item_spacing) * len(self.button_texts) - (
                            self.menu_item_height + self.menu_item_spacing)) / 2)
            if text[1] == "button":
                button = Button(menu_item_rect, text, self.font, menu_name)
                self.menu_items.append(button)
            if text[1] == "input box":
                input_box = InputBox(menu_item_rect, text, self.font, menu_name)
                self.menu_items.append(input_box)
            if text[1] == "display box":
                display_box = DisplayBox(menu_item_rect, text, self.font, menu_name)
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
                    return button_clicked
                else:
                    menu_item.active = False
        if event.type == pygame.KEYDOWN:
            for menu_item in self.menu_items:
                if menu_item.active:
                    if event.key == pygame.K_RETURN and menu_item.incorrect_value():
                        print(menu_item.text[0])
                        menu_item.active = False
                    elif event.key == pygame.K_BACKSPACE:
                        menu_item.text[0] = menu_item.text[0][:-1]
                    else:
                        menu_item.text[0] += event.unicode
                    # Re-render the text.
                    menu_item.txt_surface = pygame.font.Font(None, 32).render(menu_item.text[0], True, menu_item.color)

        return None

    def update(self):
        for menu_items in self.menu_items:
            menu_items.update()
