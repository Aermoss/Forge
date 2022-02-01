from aerforge import *
from aerforge.math import *

import pygame

class Input:
    def __init__(self):
        self.key = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

    def update(self):
        self.key = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

    def key_pressed(self, key = None):
        return self.key[key]

    def mouse_pressed(self, button = None):
        return self.mouse[button]

    def mouse_pos(self):
        return Vec2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    def mouse_rel(self):
        return pygame.mouse.get_rel()