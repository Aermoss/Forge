import pygame

from aerforge.color import *

class Polygon:
    def __init__(self, window, points, color = Color(240, 240, 240), add_to_objects = True):
        self.window = window
        
        self.color = color
        self.points = points

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
                pygame.draw.polygon(self.window.window, self.color, self.points)

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def add_points(self, points):
        self.points.append(points)

    def remove_points(self, points):
        self.points.pop(self.points.index(points))

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