from aerforge import *

import pygame

class Input:
    def __init__(self):
        self.key = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

        self.pressed_key_name = ""

        self.key_press_bool = False
        self.mouse_press_bool = False
        self.mouse_motion_bool = False

    def update(self):
        self.key = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

    def key_pressed(self, key = ""):
        if key == "":
            return self.key_press_bool

        else:
            return self.key[key]

    def mouse_pressed(self, button = ""):
        if button == "":
            return self.mouse_press_bool

        else:
            return self.mouse[button]

    def mouse_motion(self):
        return self.mouse_motion_bool

    def mouse_pos(self):
        return pygame.mouse.get_pos()

    def mouse_rel(self):
        return pygame.mouse.get_rel()