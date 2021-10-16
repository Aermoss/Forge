import pygame

from aerforge.error import ForgeError

class Mixer:
    def __init__(self, file, volume = 1.0):
        self.file = file
        self.volume = volume

        self.audio = pygame.mixer.Sound(self.file)
        self.audio.set_volume(self.volume)

    def play(self, loop = False):
        if loop:
            self.audio.play(-1)

        elif not loop:
            self.audio.play()

        else:
            raise ForgeError("Loop argument is should be bool")

    def stop(self):
        self.audio.stop()

    def pause(self):
        self.audio.pause()

    def unpause(self):
        self.audio.unpause()

    def fadeout(self, time):
        self.audio.fadeout(time)

    def set_volume(self, volume):
        self.volume = volume
        self.audio.set_volume(self.volume)

    def set_file(self, file):
        self.stop()
        self.file = file
        self.audio = pygame.mixer.Sound(self.file)
        self.audio.set_volume(self.volume)
        self.play()