from aerforge import *
from aerforge.math import *

import pygame

class Input:
    def __init__(self):
        self.held_keys = pygame.key.get_pressed()
        self.held_buttons = pygame.mouse.get_pressed()
        self.pressed = ""

    def update(self, event = None):
        if event != None:
            self.pressed = pygame.key.name(event.key)

        else:
            self.pressed = ""

        self.held_keys = pygame.key.get_pressed()
        self.held_buttons = pygame.mouse.get_pressed()

    def key_pressed(self, key = None):
        if key == None:
            return True in self.held_keys

        return self.held_keys[key]

    def mouse_pressed(self, button = None):
        if button == None:
            return True in self.held_buttons

        return self.held_buttons[button]

    def get_pressed(self):
        return self.pressed

    def mouse_pos(self):
        return Vec2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    def mouse_rel(self):
        return Vec2(pygame.mouse.get_rel()[0], pygame.mouse.get_rel()[1])

    def set_mouse_lock(self, lock):
        pygame.event.set_grab(lock)

    def set_mouse_visible(self, visible):
        pygame.mouse.set_visible(visible)

    def set_mouse_pos(self, pos):
        pygame.mouse.set_pos(pos)

    def is_key_focused(self):
        return pygame.key.get_focused()

    def is_mouse_focused(self):
        return pygame.mouse.get_focused()