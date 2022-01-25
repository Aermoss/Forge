import pygame

import time
import os

from aerforge.input import *
from aerforge.error import *
from aerforge.color import *
from aerforge.shape import *
from aerforge.entity import *
from aerforge.sprite import *

import __main__

def init():
    pygame.init()

class Forge:
    def __init__(self, width = 1200, height = 600, background_color = Color(20, 20, 20), fullscreen = False, frame = True, doublebuf = False, opengl = False, fade = True, logo = True, fps = 60):
        self.width = width
        self.height = height
        self.fps = fps

        self.background_color = background_color

        pygame.init()

        self.destroyed = False

        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.dt = 0

        self.fullscreen = fullscreen
        self.frame = frame
        self.opengl = opengl
        self.doublebuf = doublebuf

        self.path = os.path.dirname(os.path.abspath(__file__))

        try:
            pygame.display.set_icon(pygame.image.load(os.path.join(self.path, "./assets/icon/icon.png")))

        except:
            pygame.display.set_icon(pygame.image.load("icon.png"))

        pygame.display.set_caption("Forge")

        self.build_window()

        self.window.fill(self.background_color)

        try:
            self.logo = Sprite(self, os.path.join(self.path, "./assets/logo/logo.png"), width = 380, height = 80, add_to_objects = False)
            self.logo.center()

        except:
            self.logo = Sprite(self, "logo.png", width = 380, height = 80, add_to_objects = False)
            self.logo.center()

        if not logo:
            self.logo.destroy()

        self.fade = Entity(self, color = Color(0, 0, 0), width = self.width, height = self.height, add_to_objects = False)

        if not fade:
            self.fade.destroy()

        self.input = Input()

        self.keys = {
            "ESCAPE" : pygame.K_ESCAPE,

            "UP" : pygame.K_UP, "DOWN" : pygame.K_DOWN,
            "LEFT" : pygame.K_LEFT, "RIGHT" : pygame.K_RIGHT,

            "A" : pygame.K_a, "B" : pygame.K_b, "C" : pygame.K_c,
            "D" : pygame.K_d, "E" : pygame.K_e, "F" : pygame.K_f,
            "G" : pygame.K_g, "H" : pygame.K_h, "I" : pygame.K_i,
            "J" : pygame.K_j, "K" : pygame.K_k, "L" : pygame.K_l,
            "M" : pygame.K_m, "N" : pygame.K_n, "O" : pygame.K_o,
            "P" : pygame.K_p, "Q" : pygame.K_q, "R" : pygame.K_r,
            "S" : pygame.K_s, "T" : pygame.K_t, "U" : pygame.K_u,
            "V" : pygame.K_v, "W" : pygame.K_w, "X" : pygame.K_x,
            "Y" : pygame.K_y, "Z" : pygame.K_z,
    
            "0" : pygame.K_0, "1" : pygame.K_1, "2" : pygame.K_2, 
            "3" : pygame.K_3, "4" : pygame.K_4, "5" : pygame.K_5,
            "6" : pygame.K_6, "7" : pygame.K_7, "8" : pygame.K_8,
            "9" : pygame.K_9,

            "F1" : pygame.K_F1, "F2" : pygame.K_F2, "F3" : pygame.K_F3,
            "F4" : pygame.K_F4, "F5" : pygame.K_F5, "F6" : pygame.K_F6,
            "F7" : pygame.K_F7, "F8" : pygame.K_F8, "F9" : pygame.K_F9,
            "F10" : pygame.K_F10, "F11" : pygame.K_F11, "F12" : pygame.K_F12,

            "LCTRL" : pygame.K_LCTRL, "RCTRL" : pygame.K_RCTRL,
            "LSHIFT" : pygame.K_LSHIFT, "RSHIFT" : pygame.K_RSHIFT,
            "LALT" : pygame.K_LALT, "RALT" : pygame.K_RALT,

            "TAB" : pygame.K_TAB, "CAPSLOCK" : pygame.K_CAPSLOCK,

            "HOME" : pygame.K_HOME, "END" : pygame.K_END,
            "INSERT" : pygame.K_INSERT, "DELETE" : pygame.K_DELETE, 

            "RETURN" : pygame.K_RETURN, "BACKSPACE" : pygame.K_BACKSPACE, 
            "SPACE" : pygame.K_SPACE, 

            "PLUS" : pygame.K_PLUS, "MINUS" : pygame.K_MINUS, 
            "SLASH" : pygame.K_SLASH, "BACKSLASH" : pygame.K_BACKSLASH,
            "ASTERISK" : pygame.K_ASTERISK, 
        }

        self.buttons = {
            "LEFT" : 0, "MIDDLE" : 1, "RIGHT" : 2,
            "SCROLLUP" : 3, "SCROLLDOWN" : 4,
        }

        self.objects = []

        self.dt = 0
        self.clock.tick(self.fps)

    def build_window(self):
        if self.fullscreen:
            if self.opengl:
                self.window = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.OPENGL)
            
            else:
                if self.doublebuf:
                    self.window = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN | pygame.DOUBLEBUF)

                else:
                    self.window = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)

        else:
            if self.opengl:
                if not self.frame:
                    self.window = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.OPENGL, pygame.NOFRAME)

                else:
                    self.window = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.OPENGL)

            else:
                if self.doublebuf:
                    if not self.frame:
                        self.window = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF, pygame.NOFRAME)

                    else:
                        self.window = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)

                else:
                    if not self.frame:
                        self.window = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)

                    else:
                        self.window = pygame.display.set_mode((self.width, self.height))

    def run(self):
        animation_done = False
        window_fade = False
        logo_fade = False

        while True:
            self.dt = self.clock.tick(self.fps) / 1000.0

            if hasattr(__main__, "update") and __main__.update:
                __main__.update()

            for object in self.objects:
                if not object.destroyed:
                    if object.visible:
                        object.draw()

                    for script in object.scripts:
                        if hasattr(script, "update") and script.update:
                            script.update(object)

                    if hasattr(object, "update") and object.update:
                        object.update()

            if not animation_done:
                if self.logo.get_alpha() > 0:
                    if self.start_time + 6 < time.time():
                        logo_fade = True

                    if logo_fade:
                        self.logo.set_alpha(self.logo.get_alpha() - 1.2)

                    self.logo.draw()

                else:
                    animation_done = True

                if self.fade.get_alpha() > 0:
                    if self.start_time + 1 < time.time():
                        window_fade = True

                    if window_fade:
                        self.fade.set_alpha(self.fade.get_alpha() - 0.6)

                    self.fade.draw()

            pygame.display.flip()

            self.input.update()

            if self.input._key_pressed:
                self.input._key_name = ""
                self.input._key_pressed = False

            if self.input._mouse_motion:
                self.input._mouse_motion = False

            if self.input._mouse_pressed:
                self.input._mouse_pressed = False

            if self.input._scroll_up:
                self.input._scroll_up = False

            if self.input._scroll_down:
                self.input._scroll_down = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    self.input._key_name = event.unicode
                    self.input._key_pressed = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.input._mouse_pressed = True

                    if event.button == 4:
                        self.input._scroll_up = True

                    if event.button == 5:
                        self.input._scroll_down = True

                if event.type == pygame.MOUSEMOTION:
                    self.input._mouse_motion = True

            self.window.fill(self.background_color)

            if self.destroyed:
                pygame.quit()
                quit()

    def destroy(self, entity = None):
        if entity == None:
            self.destroyed = True

        else:
            entity.destroy()

    def get_fps(self):
        return self.clock.get_fps()

    def destroyall(self):
        for i in self.objects:
            i.destroy()

    def set_mouse_lock(self, lock):
        pygame.event.set_grab(lock)

    def set_mouse_visible(self, visible):
        pygame.mouse.set_visible(visible)

    def set_mouse_pos(self, pos):
        pygame.mouse.set_pos(pos)

    def minimize(self):
        pygame.display.iconify()

    def is_focused(self):
        return pygame.key.get_focused()

    def is_mouse_focused(self):
        return pygame.mouse.get_focused()

    def get_hwnd(self):
        return pygame.display.get_wm_info()["window"]

    def get_fonts(self):
        return pygame.font.get_fonts()

    def draw(self, shape = Rect, color = Color(240, 240, 240), fill = True, x = 0, y = 0, width = 200, height = 200, points = []):
        fill = not fill
        
        if shape == Rect:
            pygame.draw.rect(self.window, color, (x, y, width, height), fill)

        elif shape == Circle:
            pygame.draw.ellipse(self.window, color, (x, y, width, height), fill)

        elif shape == Polygon:
            pygame.draw.polygon(self.window, color, points, fill)

        elif shape == Line:
            for point in points:
                pygame.draw.aaline(self.window, color, point[0], point[1])

        else:
            raise ForgeError("Invalid shape")