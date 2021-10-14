from aerforge import *

import pygame

class Input:
    def __init__(self):
        self.key = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

        self._pressed_key = ""

        self._key_pressed = False
        self._mouse_pressed = False
        self._mouse_motion = False

        self._scroll_up = False
        self._scroll_down = False

    def update(self):
        self.key = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

    def key_pressed(self, key = None):
        if key == None:
            return self._key_pressed

        else:
            return self.key[key]

    def mouse_pressed(self, button = None):
        if button == None:
            return self._mouse_pressed

        else:
            if button == 3:
                return self._scroll_up

            elif button == 4:
                return self._scroll_down

            else:
                return self.mouse[button]

    def mouse_motion(self):
        return self._mouse_motion

    def mouse_pos(self):
        return pygame.mouse.get_pos()

    def mouse_rel(self):
        return pygame.mouse.get_rel()