import pygame

from aerforge.error import *
from aerforge.shape import *

class GameObject(pygame.Rect):
    def __init__(self, window, shape = "rect", width = 20, height = 20, x = 0, y = 0, color = "white"):
        self.shape = shape
        self.width = width
        self.height = height

        self.window = window
        self.color = color

        self.x = x
        self.y = y
        self.position = (self.x, self.y)

    def draw(self):
        if self.shape == Rect:
            pygame.draw.rect(self.window.window, self.color, self)

        elif self.shape == Circle:
            pygame.draw.ellipse(self.window.window, self.color, self)

    def center(self):
        self.x = self.window.width / 2 - self.width / 2
        self.y = self.window.height / 2 - self.height / 2

    def center_x(self):
        self.x = self.window.width / 2 - self.width / 2

    def center_y(self):
        self.y = self.window.height / 2 - self.height / 2