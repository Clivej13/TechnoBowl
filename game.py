import pygame

import image_alteration
from logger import Logger
from sprite import Sprite


class Game:
    def __init__(self, screen, background_image):
        self.logger = Logger()
        self.screen = screen
        self.background_image = background_image
        self.sprites = []
        sprite = Sprite(0, 0, "images/footballer.png", 66, 66, 4, False, 6, False)
        sprite2 = Sprite(100, 100, "images/footballer_new.png", 66, 66, 4, False, 6, True)
        self.sprites.append(sprite)
        self.sprites.append(sprite2)

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        for sprite in self.sprites:
            sprite.draw(self.screen)

    def handle_event(self, event):
        for sprite in self.sprites:
            if sprite.player_selected:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        sprite.set_movement(-1, 0, 1, True)
                        self.logger.log("Left")
                    if event.key == pygame.K_RIGHT:
                        sprite.set_movement(1, 0, 2, True)
                        self.logger.log("Right")
                    if event.key == pygame.K_UP:
                        sprite.set_movement(0, -1, 3, True)
                        self.logger.log("Up")
                    if event.key == pygame.K_DOWN:
                        sprite.set_movement(0, 1, 0, True)
                        self.logger.log("Down")
                    if event.key == pygame.K_SPACE:
                        self.logger.log("Space")
                    if event.key == pygame.K_ESCAPE:
                        self.logger.log("Pause")
                        return "Pause"
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        sprite.set_movement(0, 0, 1, False)
                        self.logger.log("Left")

                    if event.key == pygame.K_RIGHT:
                        sprite.set_movement(0, 0, 2, False)
                        self.logger.log("Right")
                    if event.key == pygame.K_UP:
                        sprite.set_movement(0, 0, 3, False)
                        self.logger.log("Up")
                    if event.key == pygame.K_DOWN:
                        sprite.set_movement(0, 0, 0, False)
                        self.logger.log("Down")
                    if event.key == pygame.K_SPACE:
                        self.logger.log("Space")
                return None

    def update(self):
        for sprite in self.sprites:
            sprite.update()
