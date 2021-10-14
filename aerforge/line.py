import pygame

from aerforge import *

class Line:
    def __init__(self, window, start_x = 0, start_y = 0, end_x = 0, end_y = 0, color = Color(240, 240, 240), add_to_objects = True):
        self.window = window
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

        self.destroyed = False

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def draw(self):
        if not self.destroyed:
            start_pos = (self.start_x, self.start_y)
            end_pos = (self.end_x, self.end_y)
            pygame.draw.aaline(self.window.window, self.color, start_pos, end_pos)

    def destroy(self):
        self.destroyed = True