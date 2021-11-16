import pygame
import cv2

from aerforge.error import ForgeError

class Movie:
    def __init__(self, window, file, width = 200, height = 200, x = 0, y = 0, add_to_objects = True):
        self.window = window

        self.file = file

        self.width = width
        self.height = height

        self.x = x
        self.y = y

        self.video = cv2.VideoCapture(self.file)
        success, video_image = self.video.read()

        if not success:
            raise ForgeError("Failed to load video")

        self.scripts = []

        self.destroyed = False

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def _update(self):
        if not self.destroyed:
            for script in self.scripts:
                script.update(self)

    def draw(self):
        if not self.destroyed:
            success, video_image = self.video.read()

            if not success:
                raise ForgeError("Failed to load video")

            video_image = cv2.resize(video_image, (self.width, self.height))

            video_surface = pygame.image.frombuffer(video_image.tobytes(), (self.width, self.height), "BGR")

            self.window.window.blit(video_surface, (self.x, self.y))

    def load_video(self, file):
        self.file = file

        self.video = cv2.VideoCapture(self.file)
        success, video_image = self.video.read()

        if not success:
            raise ForgeError("Failed to load video")

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