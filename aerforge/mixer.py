import pygame

class Mixer:
    def __init__(self, window, file, volume = 1.0, add_to_objects = True):
        self.window = window
        self.file = file
        self.volume = volume

        self.audio = pygame.mixer.Sound(self.file)
        self.audio.set_volume(self.volume)

        self.scripts = []

        self.destroyed = False
        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def update(self):
        pass

    def play(self, loop = 0):
        if not self.destroyed:
            self.audio.play(loop)

    def stop(self):
        if not self.destroyed:
            self.audio.stop()

    def pause(self):
        if not self.destroyed:
            self.audio.pause()

    def unpause(self):
        if not self.destroyed:
            self.audio.unpause()

    def fade_in(self, duration = 1000, loop = 0):
        if not self.destroyed:
            self.audio.play(loop, fade_ms = duration)

    def fade_out(self, duration = 1000):
        if not self.destroyed:
            self.audio.fadeout(duration)

    def set_volume(self, volume):
        if not self.destroyed:
            self.volume = volume
            self.audio.set_volume(self.volume)

    def set_file(self, file):
        if not self.destroyed:
            self.stop()
            self.file = file
            self.audio = pygame.mixer.Sound(self.file)
            self.audio.set_volume(self.volume)
            self.play()

    def destroy(self):
        self.destroyed = True
        self.stop()

        if self.add_to_objects:
            try:
                self.window.objects.pop(self.window.objects.index(self))

            except:
                pass

    def add_script(self, script):
        self.scripts.append(script)

    def remove_script(self, script):
        self.scripts.pop(self.scripts.index(script))