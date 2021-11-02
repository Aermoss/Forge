import pygame

from aerforge.error import *

class Sprite(pygame.Rect):
    def __init__(self, window, file, width = 1200, height = 600, x = 0, y = 0, add_to_objects = True):
        self.window = window

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.file = file
        self.image = pygame.image.load(self.file)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rotated_image = self.image
        self.rotated_image_rect = self.rotated_image.get_rect(center = (self.x + self.width / 2, self.y + self.height / 2))

        self.angle = 0

        self.destroyed = False
        self.rotated = False

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def draw(self):
        if not self.destroyed:
            if self.angle != 0:
                self.rotated = True

            if self.rotated:
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.rotated_image = pygame.transform.rotozoom(self.image, self.angle, 1)
                self.rotated_image_rect = self.rotated_image.get_rect(center = (self.x + self.width / 2, self.y + self.height / 2))
                self.window.window.blit(self.rotated_image, self.rotated_image_rect)

            else:
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.window.window.blit(self.image, (self.x, self.y))

    def rotate(self, angle):
        self.rotated = True
        self.angle = angle

    def set_image(self, file):
        self.file = file
        self.image = pygame.image.load(self.file)

    def get_alpha(self):
        return self.image.get_alpha()

    def set_alpha(self, alpha):
        self.image.set_alpha(alpha)

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

        if self.add_to_objects:
            try:
                self.window.objects.pop(self.window.objects.index(self))

            except:
                pass

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