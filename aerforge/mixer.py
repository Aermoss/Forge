import pygame

class Mixer:
    def __init__(self, file, volume):
        self.file = file
        self.volume = volume

        self.audio = pygame.mixer.Sound(self.file)
        self.audio.set_volume(self.volume)

    def play(self):
        self.audio.play()

    def stop(self):
        self.audio.stop()