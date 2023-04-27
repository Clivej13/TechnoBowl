import pygame

from logger import Logger


class Sprite:
    def __init__(self, x, y, image_path, frame_width, frame_height, num_frames, moving, speed, player_selected):
        self.player_selected = player_selected
        self.logger = Logger()
        self.speed = speed
        self.direction = 0
        self.moving = moving
        self.x_movement = 0
        self.y_movement = 0
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.frame_width = frame_width
        self.frame_height = frame_height
        self.num_frames = num_frames
        self.frame_index = 0
        self.frame_counter = 0

    def draw(self, screen):
        frame_x = (self.frame_index % self.num_frames) * self.frame_width
        frame_y = self.direction * self.frame_height
        frame_rect = pygame.Rect(frame_x, frame_y, self.frame_width, self.frame_height)
        screen.blit(self.image, (self.x, self.y), frame_rect)

    def move(self, dx, dy, direction):
        if self.moving:
            self.direction = direction
            self.x += dx
            self.y += dy
            self.rect.x = self.x
            self.rect.y = self.y

            self.frame_counter += 1
            if self.frame_index == 3:
                self.frame_index = 0
            if self.frame_counter >= 1:  # Change frame every 10 move events
                self.frame_index = (self.frame_index + 1) % (self.num_frames * (self.frame_index < 3))
                self.frame_counter = 0

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)

    def update(self):
        self.move(self.x_movement, self.y_movement, self.direction)
        pass

    def set_movement(self, x_movement, y_movement, direction, moving):
        self.moving = moving
        self.direction = direction
        self.x_movement = x_movement * self.speed
        self.y_movement = y_movement * self.speed
        self.logger.log(str(direction) + " " + str(x_movement) + " " + str(y_movement))
        pass

    def get_rect(self):
        return self.rect

    def scale(self, scale_factor):
        self.frame_width = int(self.frame_width * scale_factor)
        self.frame_height = int(self.frame_height * scale_factor)
        self.image = pygame.transform.scale(self.image, (self.frame_width * self.num_frames, self.frame_height * 4))
