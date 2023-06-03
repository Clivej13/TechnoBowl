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
        self.display_text = data["menu_item_value"]
        self.active = False
        self.expandable = False
        self.logger = Logger()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        txt_surface = self.font.render(self.display_text, True, (0, 0, 0))
        # Blit the text.
        surface.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.

    def on_click(self):
        self.incorrect = False
        if not self.active:
            self.active = True
        self.display_text = self.data["menu_item_value"]
        return [self.data, self.menu_name, self.incorrect]

    def update(self):
        if self.data["menu_item_value"] == "":
            self.display_text = self.data["menu_item_data"]
        else:
            self.display_text = self.data["menu_item_value"]
        if self.active:
            self.color = (135, 206, 235)
            self.display_text = self.data["menu_item_value"]
        elif not self.active:
            self.color = (255, 255, 255)
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.color = self.hover_color
        if self.incorrect:
            self.color = (255, 0, 51)
            self.display_text = self.data["menu_item_data"]
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.color = self.hover_color
        if self.data["menu_item_value"] == "\r":
            self.data["menu_item_value"] = ""

    def deselect(self):
        if self.active:
            self.active = False

    def incorrect_value(self):
        if self.data["menu_item_validation"] == "Color":
            try:
                list_rgb = self.data["menu_item_value"].split(",")
                if int(list_rgb[0]) > 0 or int(list_rgb[0]) < 255 and int(list_rgb[1]) > 0 or int(
                        list_rgb[1]) < 255 and int(list_rgb[2]) > 0 or int(list_rgb[2]) < 255:
                    self.incorrect = False
                    return True
                else:
                    self.incorrect = True
                    self.data["menu_item_value"] = ""
                    return False
            except Exception as e:
                self.incorrect = True
                self.data["menu_item_value"] = ""
                return False
        if self.data["menu_item_validation"] == "Text":
            if self.data["menu_item_value"] == "":
                self.incorrect = True
                return False
            else:
                self.incorrect = False
        return True
