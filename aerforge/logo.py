from aerforge.sprite import Sprite
from aerforge.entity import Entity
from aerforge.color import Color

import time
import os

class Logo:
    def __init__(self, window):
        self.window = window
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.start_time = time.time()

        try:
            self.logo = Sprite(window, os.path.join(self.path, "./assets/logo/logo.png"), width = 380, height = 80, add_to_objects = False)
            self.logo.center()

        except:
            self.logo = Sprite(window, "logo.png", width = 380, height = 80, add_to_objects = False)
            self.logo.center()

        self.fade = Entity(window, color = Color(0, 0, 0), width = window.width, height = window.height, add_to_objects = False)
        
        self.destroyed = False
        self.fade_done = False
        self.logo_done = False

    def update(self):
        if not self.destroyed:
            self.logo.center()
            self.fade.width, self.fade.height = self.window.width, self.window.height

            if self.logo.get_alpha() > 0:
                if self.start_time + 6 < time.time():
                    self.logo_done = True

                if self.logo_done:
                    self.logo.set_alpha(self.logo.get_alpha() - 1.2)

                self.logo.draw()

            else:
                self.destroy()

            if self.fade.get_alpha() > 0:
                if self.start_time + 1 < time.time():
                    self.fade_done = True

                if self.fade_done:
                    self.fade.set_alpha(self.fade.get_alpha() - 0.6)

                self.fade.draw()

    def destroy(self):
        self.logo.destroy()
        self.fade.destroy()
        self.destroyed = True