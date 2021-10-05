import pygame

class Camera:
    def __init__(self, window):
        self.window = window

    def set_pos(self, x, y):
        for i in self.window.objects:
            i.x = i.x - (x - self.window.width / 2)
            i.y = i.y - (y - self.window.height / 2)