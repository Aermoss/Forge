import pygame

from aerforge import *

class Entity(pygame.Rect):
    def __init__(self, window, shape = Rect, width = 50, height = 50, x = 0, y = 0, color = Color(240, 240, 240), points = [], add_to_objects = True):
        self.window = window

        self.width = width
        self.height = height

        self.x = x
        self.y = y

        self.shape = shape
        self.color = color

        self.points = points

        self.destroyed = False

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def draw(self):
        if not self.destroyed:
            if self.shape == Rect:
                pygame.draw.rect(self.window.window, self.color, self)

            elif self.shape == Circle:
                pygame.draw.ellipse(self.window.window, self.color, self)

            elif self.shape == Polygon:
                pygame.draw.polygon(self.window.window, self.color, self.points)

            else:
                raise ForgeError("Invalid shape")

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def center(self):
        self.x = self.window.width / 2 - self.width / 2
        self.y = self.window.height / 2 - self.height / 2

    def center_x(self):
        self.x = self.window.width / 2 - self.width / 2

    def center_y(self):
        self.y = self.window.height / 2 - self.height / 2

    def hit(self, entity):
        if isinstance(entity, pygame.Rect):
            return self.colliderect(entity)

        elif isinstance(entity, tuple):
            return self.collidepoint(entity)

        else:
            raise ForgeError("Invalid type")

    def hit2(self, entity, collision_tolreance = 10):
        if self.hit(entity):
            if abs(entity.top - self.bottom) < collision_tolreance:
                return "bottom"

            elif abs(entity.bottom - self.top) < collision_tolreance:
                return "top"

            elif abs(entity.right - self.left) < collision_tolreance:
                return "left"

            elif abs(entity.left - self.right) < collision_tolreance:
                return "right"

            else:
                return "unknown"
        
        else:
            return ""

    def destroy(self):
        self.destroyed = True

        if self.add_to_objects:
            try:
                self.window.objects.pop(self.window.objects.index(self))

            except:
                pass