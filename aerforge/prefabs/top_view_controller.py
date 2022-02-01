from aerforge import *

class TopViewController(Entity):
    def __init__(self, window, shape = shape.Rect, x = 0, y = 0, width = 50, height = 100, color = color.Color(240, 240, 240), sprint_speed = 6, walk_speed = 3):
        super().__init__(
            window = window,
            shape = shape,
            width = width,
            height = height,
            x = x,
            y = y,
            color = color,
        )

        self.speed = 0
        self.sprint_speed = sprint_speed
        self.walk_speed = walk_speed

    def update(self):
        if self.window.input.key_pressed(self.window.keys["LSHIFT"]):
            self.speed = self.sprint_speed

        else:
            self.speed = self.walk_speed

        if self.window.input.key_pressed(self.window.keys["W"]):
            self.y = self.y - self.speed

        if self.window.input.key_pressed(self.window.keys["S"]):
            self.y = self.y + self.speed

        if self.window.input.key_pressed(self.window.keys["A"]):
            self.x = self.x - self.speed

        if self.window.input.key_pressed(self.window.keys["D"]):
            self.x = self.x + self.speed