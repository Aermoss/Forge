import pygame

class Mixer:
    def __init__(self, file, volume = 1.0):
        self.file = file
        self.volume = volume

        self.audio = pygame.mixer.Sound(self.file)
        self.audio.set_volume(self.volume)

    def play(self, loop = 0):
        self.audio.play(loop)

    def stop(self):
        self.audio.stop()

    def pause(self):
        self.audio.pause()

    def unpause(self):
        self.audio.unpause()

    def fade_in(self, duration = 1000, loop = 0):
        self.audio.play(loop, fade_ms = duration)

    def fade_out(self, duration = 1000):
        self.audio.fadeout(duration)

    def set_volume(self, volume):
        self.volume = volume
        self.audio.set_volume(self.volume)

    def set_file(self, file):
        self.stop()
        self.file = file
        self.audio = pygame.mixer.Sound(self.file)
        self.audio.set_volume(self.volume)
        self.play()