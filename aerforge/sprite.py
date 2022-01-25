import pygame

from aerforge import *

class Sprite(pygame.Rect):
    def __init__(self, window, file, alpha = 255, width = 200, height = 200, x = 0, y = 0, add_to_objects = True):
        self.window = window

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.alpha = alpha

        self.file = file
        self.image = pygame.image.load(self.file)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rotated_image = self.image
        self.rotated_image_rect = self.rotated_image.get_rect(center = (self.x + self.width / 2, self.y + self.height / 2))

        self.angle = 0

        self.scripts = []

        self.destroyed = False
        self.visible = True
        self.rotated = False

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def update(self):
        pass

    def draw(self):
        if not self.destroyed:
            if self.visible:
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
        self.alpha = self.image.get_alpha()
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.image.set_alpha(self.alpha)

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

    def hit(self, entity):
        if isinstance(entity, Vec2):
            return self.collidepoint((entity.x, entity.y))

        else:
            return self.colliderect(entity)

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

    def add_script(self, script):
        self.scripts.append(script)

    def remove_script(self, script):
        self.scripts.pop(self.scripts.index(script))

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