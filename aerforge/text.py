import pygame

from aerforge.color import *
from aerforge.error import *

class Text:
    def __init__(self, window, text, font_size = 24, font_file = None, font_name = "arial", bold = False, italic = False, underline = False, color = Color(240, 240, 240), x = 0, y = 0, add_to_objects = True):
        self.window = window

        self.x = x
        self.y = y

        self.font_file = font_file
        self.font_name = font_name
        self.font_size = font_size

        self.bold = bold
        self.italic = italic
        self.underline = underline

        self.load_font(self.font_file, self.font_name)
        self.set_bold(self.bold)
        self.set_italic(self.italic)
        self.set_underline(self.underline)
        
        self.color = color
        self.text = text

        self.scripts = []

        self.destroyed = False
        self.visible = True

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def update(self):
        pass

    def draw(self):
        if not self.destroyed:
            if self.visible:
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

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_font_size(self):
        return self.font_size

    def set_font_size(self, font_size):
        self.font_size = font_size
        self.load_font(self.font_file, self.font_name)

    def get_font_file(self):
        return self.font_file

    def get_font_name(self):
        return self.font_name

    def set_bold(self, bold):
        self.bold = bold
        self.font.set_bold(self.bold)

    def set_italic(self, italic):
        self.italic = italic
        self.font.set_italic(self.italic)

    def set_underline(self, underline):
        self.underline = underline
        self.font.set_underline(self.underline)

    def get_bold(self):
        return self.bold

    def get_italic(self):
        return self.italic

    def get_underline(self):
        return self.underline

    def load_font(self, font_file = None, font_name = "arial"):
        self.font_file = font_file
        self.font_name = font_name

        if self.font_file != None:
            self.font = pygame.font.Font(self.font_file, self.font_size)

        else:
            self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def get_width(self):
        rendered_text = self.font.render(self.text, True, self.color)
        return rendered_text.get_width()

    def get_height(self):
        rendered_text = self.font.render(self.text, True, self.color)
        return rendered_text.get_height()

    def center(self):
        self.x = self.window.width / 2 - self.get_width() / 2
        self.y = self.window.height / 2 - self.get_height() / 2

    def center_x(self):
        self.x = self.window.width / 2 - self.get_width() / 2

    def center_y(self):
        self.y = self.window.height / 2 - self.get_height() / 2

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