import pygame

class Color(pygame.Color):
    def __init__(self, r, g, b, a = 255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a