from aerforge import *
import math
import time

class Gun:
    def __init__(self, window, player):
        self.window = window
        self.player = player
        self.bullet_speed = 30
        self.all_bullets = []
        self.state = True
        self.last_shoot = time.time()
        self.shoot_time = 0.1
        self.magazine_size = 20
        self.bullets = self.magazine_size
        self.reload_start_time = time.time()
        self.reload_time = 2.4
        self.reloading = False
        self.selected = True
        self.automatic = False

    def reload(self):
        if not self.reloading:
            self.reloading = True
            self.reload_start_time = time.time()

    def shoot(self):
        mouse_x, mouse_y = self.window.input.mouse_pos()
                    
        distance_x = mouse_x - self.player.x
        distance_y = mouse_y - self.player.y
        
        angle = math.atan2(distance_y, distance_x)

        speed_x = self.bullet_speed * math.cos(angle)
        speed_y = self.bullet_speed * math.sin(angle)

        self.all_bullets.append([self.player.x + (self.player.width / 2), self.player.y + (self.player.height / 2 - 45), speed_x, speed_y])

    def get_input(self):
        if self.window.input.key_pressed(self.window.keys["R"]):
            if self.bullets != self.magazine_size:
                self.reload()

        if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
            if self.state:
                if not self.reloading:
                    if self.bullets > 0:
                        self.shoot()
                        self.state = False
                        self.last_shoot = time.time()
                        self.bullets = self.bullets - 1
        
        else:
            if not self.automatic:
                if self.last_shoot + self.shoot_time < time.time():
                    self.state = True

    def update(self):
        if self.selected:
            if self.bullets <= 0:
                self.reload()

            if self.automatic:
                if self.last_shoot + self.shoot_time < time.time():
                    self.state = True

            self.get_input()

            if self.reloading:
                if self.reload_start_time + self.reload_time < time.time():
                    self.reloading = False
                    self.bullets = self.magazine_size

        else:
            self.reloading = False

        for item in self.all_bullets:
            item[0] = item[0] + item[2]
            item[1] = item[1] + item[3]

        for pos_x, pos_y, speed_x, speed_y in self.all_bullets:
            if pos_x > self.window.width or pos_x < 0 or pos_y > self.window.height or pos_y < 0:
                self.all_bullets.pop(self.all_bullets.index([pos_x, pos_y, speed_x, speed_y]))

            else:
                self.window.draw(shape = Rect, width = 10, height = 10, x = int(pos_x), y = int(pos_y))

if __name__ == "__main__":
    from aerforge.prefabs import *

    forge = Forge()

    player = TopViewController(forge)
    player.center()

    gun = Gun(forge, player)

    while True:
        player.update()
        gun.update()
        player.draw()
        forge.update()