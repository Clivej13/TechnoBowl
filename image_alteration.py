import pygame

from logger import Logger


class ImageAlteration:

    def __init__(self, image, old_color, new_color, path):
        logger = Logger()
        # Load the image surface
        image = pygame.image.load(image).convert_alpha()

        # Create a new surface with the same dimensions as the original image
        new_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)

        # Iterate over all pixels in the image and replace the old color with the new color
        for x in range(image.get_width()):
            for y in range(image.get_height()):
                pixel_color = image.get_at((x, y))
                logger.log("Pixel Color: " + str(pixel_color) + "Old Color: " + str(old_color) + "New Color: " + str(
                    new_color))
                if pixel_color == old_color:
                    new_image.set_at((x, y), new_color)
                else:
                    new_image.set_at((x, y), pixel_color)

        # Display the image on the screen
        pygame.image.save(new_image, path)

    def change_color(self):
        # Light shade main
        image_alteration.ImageAlteration("images/footballer_new.png", (123, 97, 185, 255), (147, 158, 151),
                                         "images/footballer_new.png")
        # Mid shade main
        image_alteration.ImageAlteration("images/footballer_new.png", (96, 81, 125, 255), (81, 125, 96),
                                         "images/footballer_new.png")
        # Dark shade main
        image_alteration.ImageAlteration("images/footballer_new.png", (64, 60, 81, 255), (40, 62, 48),
                                         "images/footballer_new.png")
        # Glove Color
        image_alteration.ImageAlteration("images/footballer_new.png", (78, 74, 140, 255), (64, 100, 76),
                                         "images/footballer_new.png")
        # Trim Color Light
        image_alteration.ImageAlteration("images/footballer_new.png", (253, 111, 85, 255), (111, 85, 253),
                                         "images/footballer_new.png")
        # Trim Color Dark
        image_alteration.ImageAlteration("images/footballer_new.png", (140, 23, 44, 255), (33, 25, 75),
                                         "images/footballer_new.png")

    def get_shade_highlight(self, rgb, shade_factor=0.5, highlight_factor=1.5):
        # Calculate shade value
        shade = tuple(int(c * shade_factor) for c in rgb)

        # Calculate highlight value
        highlight = tuple(min(int(c * highlight_factor), 255) for c in rgb)

        return shade, highlight
