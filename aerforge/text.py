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

        self.scripts = []

        self.destroyed = False

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def _update(self):
        if not self.destroyed:
            for script in self.scripts:
                script.update(self)

    def draw(self):
        if not self.destroyed:
            rendered_text = self.font.render(self.text, True, self.color)
            self.window.window.blit(rendered_text, (self.x, self.y))

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def center(self):
        self.x = self.window.width / 2 - (len(self.text) * (self.font_size / 3)) / 2
        self.y = self.window.height / 2 - (self.font_size / 3)

    def center_x(self):
        self.x = self.window.width / 2 - (len(self.text) * (self.font_size / 3)) / 2

    def center_y(self):
        self.y = self.window.height / 2 - (self.font_size / 3)

    def destroy(self):
        self.destroyed = True

        if self.add_to_objects:
            try:
                self.window.objects.pop(self.window.objects.index(self))

            except:
                pass

    def add_script(self, script):
        self.scripts.append(script)

    def remove_script(self, script):
        self.scripts.pop(self.scripts.index(script))