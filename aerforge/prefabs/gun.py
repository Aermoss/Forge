from aerforge import *

import math
import time

class Gun:
    def __init__(self, window, x = 0, y = 0, bullet_speed = 50, shoot_cooldown = 0.1, magazine_size = 20, selected = True, automatic = False, reload_time = 2.4):
        self.window = window

        self.x = x
        self.y = y

        self.bullet_speed = bullet_speed
        self.shoot_cooldown = shoot_cooldown
        self.magazine_size = magazine_size
        self.reload_time = reload_time
        self.selected = selected
        self.automatic = automatic

        self.bullet_count = self.magazine_size
        self.reload_start_time = time.time()
        self.last_shoot = time.time()
        self.all_bullets = []

        self.state = True
        self.reloading = False
        self.shooting = False

    def reload(self):
        if not self.reloading:
            self.reloading = True
            self.reload_start_time = time.time()

    def shoot(self):
        self.shooting = True

        mouse = self.window.input.mouse_pos()
                    
        distance_x = mouse.x - self.x
        distance_y = mouse.y - self.y
        
        angle = math.atan2(distance_y, distance_x)

        speed_x = self.bullet_speed * math.cos(angle)
        speed_y = self.bullet_speed * math.sin(angle)

        self.all_bullets.append([self.x, self.y, speed_x, speed_y])

    def get_input(self):
        if self.window.input.key_pressed(self.window.keys["R"]):
            if self.bullet_count != self.magazine_size:
                self.reload()

        if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
            if self.state:
                if not self.reloading:
                    if self.bullet_count > 0:
                        self.shoot()
                        self.state = False
                        self.last_shoot = time.time()
                        self.bullet_count = self.bullet_count - 1
        
        else:
            if not self.automatic:
                if self.last_shoot + self.shoot_cooldown < time.time():
                    self.state = True

    def update(self):
        if self.bullet_count > self.magazine_size:
            self.bullet_count = self.magazine_size

        if self.shooting:
            self.shooting = False

        if self.selected:
            if self.bullet_count <= 0:
                self.reload()

            if self.automatic:
                if self.last_shoot + self.shoot_cooldown < time.time():
                    self.state = True

            self.get_input()

            if self.reloading:
                if self.reload_start_time + self.reload_time < time.time():
                    self.reloading = False
                    self.bullet_count = self.magazine_size

        else:
            self.reloading = False

        for item in self.all_bullets:
            item[0] = item[0] + item[2]
            item[1] = item[1] + item[3]

    def draw(self):
        for pos_x, pos_y, speed_x, speed_y in self.all_bullets:
            if pos_x > self.window.width or pos_x < 0 or pos_y > self.window.height or pos_y < 0:
                self.all_bullets.pop(self.all_bullets.index([pos_x, pos_y, speed_x, speed_y]))

            else:
                self.window.draw(shape = shape.Rect, width = 10, height = 10, x = int(pos_x), y = int(pos_y))

    def is_reloading(self):
        if self.reloading:
            return True
        
        return False

    def is_shooting(self):
        if self.shooting:
            return True
        
        return False

    def hit(self, entity, destroy_bullet = False):
        for pos_x, pos_y, speed_x, speed_y in self.all_bullets:
            if entity.hit(Vec2(pos_x, pos_y)):
                if destroy_bullet:
                    self.all_bullets.pop(self.all_bullets.index([pos_x, pos_y, speed_x, speed_y]))

                return True

        return False

    def center(self):
        self.x = self.window.width / 2
        self.y = self.window.height / 2

    def center_x(self):
        self.x = self.window.width / 2

    def center_y(self):
        self.y = self.window.height / 2

    def set_magazine_size(self, magazine_size):
        self.magazine_size = magazine_size
        
        if self.bullet_count > self.magazine_size:
            self.bullet_count = self.magazine_size

    def get_magazine_size(self):
        return self.magazine_size

    def set_bullet_count(self, count):
        self.bullet_count = count

        if self.bullet_count > self.magazine_size:
            self.bullet_count = self.magazine_size

    def get_bullet_count(self):
        return self.bullet_count