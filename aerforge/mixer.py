import pygame

class Mixer:
    def __init__(self, file, volume = 1.0):
        self.file = file
        self.volume = volume

        self.audio = pygame.mixer.Sound(self.file)
        self.audio.set_volume(self.volume)

    def play(self):
        self.audio.play()

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