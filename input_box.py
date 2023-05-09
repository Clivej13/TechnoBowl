import pygame

from logger import Logger


class InputBox:
    def __init__(self, input_box_rect, data, font, menu_name):
        self.incorrect = False
        self.logger = Logger()
        self.menu_name = menu_name
        self.font = font
        self.rect = input_box_rect
        self.color = (255, 255, 255)
        self.hover_color = (200, 200, 200)
        self.clicked_color = (100, 100, 100)
        self.data = data
        self.initial_text = data["menu_item_data"]
        self.active = False
        self.logger = Logger()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        txt_surface = self.font.render(self.data["menu_item_data"], True, (0, 0, 0))
        # Blit the text.
        surface.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.

    def on_click(self):
        self.incorrect = False
        if not self.active:
            self.active = True
        if self.data["menu_item_data"] == self.initial_text:
            self.logger.log(self.data["menu_item_data"] + " match " + self.initial_text)
            self.data["menu_item_data"] = ""
        return [self.data, self.menu_name]

    def update(self):
        if self.active:
            self.color = (135, 206, 235)
        elif not self.active:
            self.color = (255, 255, 255)
            if self.data["menu_item_data"] == "":
                self.data["menu_item_data"] = self.initial_text
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.color = self.hover_color
        if self.incorrect:
            self.color = (255, 0, 51)
            self.data["menu_item_data"] = self.initial_text
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.color = self.hover_color

    def deselect(self):
        if self.active:
            self.active = False

    def incorrect_value(self):
        if self.data[1] == "Color":
            try:
                list_rgb = self.data[0].split(",")
                if int(list_rgb[0]) > 0 or int(list_rgb[0]) < 255 and int(list_rgb[1]) > 0 or int(
                        list_rgb[1]) < 255 and int(list_rgb[2]) > 0 or int(list_rgb[2]) < 255:
                    return True
                else:
                    self.deselect()
                    self.incorrect = True
                    return False
            except Exception as e:
                self.logger.log("Exception")
                self.deselect()
                self.incorrect = True
                return False
        return True
