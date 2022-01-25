from aerforge.math import Vec3

import pygame

class Color(pygame.Color):
    def __init__(self, r, g, b, a = 255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def lerp(self, color, value):
        active_color = Vec3(self.r, self.g, self.b)
        active_color.lerp(Vec3(color.r, color.g, color.b), value)
        self.r, self.g, self.b = int(active_color.x), int(active_color.y), int(active_color.z)
        
Red = Color(240, 0, 0)
Green = Color(0, 240, 0)
Blue = Color(0, 0, 240)
White = Color(240, 240, 240)
Black = Color(40, 40, 40)