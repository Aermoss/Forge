from aerforge import *

class TopViewController(GameObject):
    def __init__(self, window, shape = Rect, x = 0, y = 0, width = 50, height = 100, color = WHITE):
        super().__init__(
            window = window, 
            shape = shape, 
            width = width, 
            height = height,  
            x = x, 
            y = y,
            color = color,
        )

        self.speed = 5
        self.sprint_speed = 10
        self.walk_speed = 5

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

if __name__ == "__main__":
    forge = Forge()

    player = TopViewController(window = forge, color = (200, 120, 0))

    while True:
        player.update()
        player.draw()
        forge.update()