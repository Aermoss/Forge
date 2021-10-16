import pygame

from aerforge.error import *

class Sprite(pygame.Rect):
    def __init__(self, window, image, x = 0, y = 0, width = 200, height = 200, add_to_objects = True):
        self.window = window

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.image = image
        self.image = pygame.image.load(self.image)

        self.destroyed = False

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def draw(self):
        if not self.destroyed:
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.window.window.blit(self.image, (self.x, self.y))

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def center(self):
        self.x = self.window.width / 2 - self.width / 2
        self.y = self.window.height / 2 - self.height / 2

    def center_x(self):
        self.x = self.window.width / 2 - self.width / 2

    def center_y(self):
        self.y = self.window.height / 2 - self.height / 2

    def resize(self, size):
        self.image = pygame.transform.scale(self.image, size)

    def hit(self, gameobject):
        if isinstance(gameobject, pygame.Rect):
            return self.colliderect(gameobject)

        elif isinstance(gameobject, tuple):
            return self.collidepoint(gameobject)

        else:
            raise ForgeError("Invalid type")

    def hit2(self, gameobject, collision_tolreance = 10):
        if self.hit(gameobject):
            if abs(gameobject.top - self.bottom) < collision_tolreance:
                return "bottom"

            elif abs(gameobject.bottom - self.top) < collision_tolreance:
                return "top"

            elif abs(gameobject.right - self.left) < collision_tolreance:
                return "left"

            elif abs(gameobject.left - self.right) < collision_tolreance:
                return "right"

            else:
                return ""
        
        else:
            return ""

    def destroy(self):
        self.destroyed = True

    def play_animation(self, animation, mirror_x = False, mirror_y = False):
        animation.pos = animation.pos + animation.time

        if animation.pos >= len(animation.frames):
            animation.pos = 0

        self.image = pygame.image.load(f"{animation.folder}/{animation.frames[int(animation.pos)]}")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
        if mirror_x:
            self.image = pygame.transform.flip(pygame.transform.scale(self.image, (self.width, self.height)), True, False)
        
        if mirror_y:
            self.image = pygame.transform.flip(pygame.transform.scale(self.image, (self.width, self.height)), False, True)

        self.draw()