import pygame

class Input:
    def __init__(self):
        self.key = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

    def update(self):
        self.key = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

    def key_pressed(self, key):
        return self.key[key]

    def mouse_pressed(self, button):
        return self.mouse[button]

    def mouse_pos(self):
        return pygame.mouse.get_pos()