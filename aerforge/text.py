import pygame

from aerforge.color import *

class Text:
    def __init__(self, window, text, font_size = 24, font_file = None, color = Color(240, 240, 240), x = 0, y = 0, add_to_objects = True):
        self.window = window

        self.x = x
        self.y = y

        self.font_file = font_file
        self.font_size = font_size
        self.font = pygame.font.Font(self.font_file, self.font_size)
        
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
        self.x = self.window.width / 2 - (len(self.text) * (self.font_size / 3)) / 2
        self.y = self.window.height / 2 - (self.font_size / 3)

    def center_x(self):
        self.x = self.window.width / 2 - (len(self.text) * (self.font_size / 3)) / 2

    def center_y(self):
        self.y = self.window.height / 2 - (self.font_size / 3)

    def destroy(self):
        self.destroyed = True