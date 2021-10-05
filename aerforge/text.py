import pygame

from aerforge.color import *

class Text:
    def __init__(self, window, text, font_size = 24, file = None, color = WHITE, x = 0, y = 0, add_to_objects = True):
        self.window = window

        self.x = x
        self.y = y

        self.file = file
        self.font_size = font_size
        self.font = pygame.font.Font(self.file, self.font_size)
        
        self.color = color
        self.text = text

        self.destroyed = False

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def draw(self):
        if not self.destroyed:
            rendered_text = self.font.render(self.text, True, self.color)
            self.window.window.blit(rendered_text, (self.x, self.y))

    def center(self):
        self.x = self.window.width / 2 - self.font_size / 2
        self.y = self.window.height / 2 - self.font_size / 2

    def center_x(self):
        self.x = self.window.width / 2 - self.font_size / 2

    def center_y(self):
        self.y = self.window.height / 2 - self.font_size / 2

    def destroy(self):
        self.destroyed = True