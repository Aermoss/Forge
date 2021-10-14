from aerforge import *

class PlatformerController(GameObject):
    def __init__(self, window, shape = Rect, x = 0, y = 0, width = 50, height = 100, color = Color(240, 240, 240), jump_force = -13, gravity = 0.6, sprint_speed = 10, walk_speed = 5):
        super().__init__(
            window = window,
            shape = shape,
            width = width,
            height = height,
            x = x,
            y = y,
            color = color,
        )

        self.objects = []

        self.state = False
        self.grounded = False
        self.velocity = 0
        self.speed = 0

        self.jump_force = jump_force
        self.gravity = gravity

        self.sprint_speed = sprint_speed
        self.walk_speed = walk_speed

    def jump(self):
        self.velocity = self.velocity + self.jump_force
        self.grounded = False

    def update(self):
        self.y = self.y + self.velocity

        self.state = False

        for i in self.objects:
            if not i.destroyed:
                if self.hit(i):
                    self.y = i.y - self.height + 1
                    self.velocity = 0
                    self.grounded = True
                    self.state = True

        if not self.state:
            self.grounded = False

        self.state = False

        if not self.grounded:
            self.velocity = self.velocity + self.gravity

        if self.window.input.key_pressed(self.window.keys["SPACE"]) and self.grounded:
            self.jump()

        if self.window.input.key_pressed(self.window.keys["LSHIFT"]):
            self.speed = self.sprint_speed
        else:
            self.speed = self.walk_speed

        if self.window.input.key_pressed(self.window.keys["A"]):
            self.x = self.x - self.speed

        if self.window.input.key_pressed(self.window.keys["D"]):
            self.x = self.x + self.speed

if __name__ == "__main__":
    forge = Forge()

    ground = GameObject(window = forge, shape = Rect, width = 1200, height = 100, color = (50, 50, 100))
    ground.y = 500

    player = PlatformerController(window = forge, color = Color(200, 120, 0))
    player.objects.append(ground)

    while True:
        player.update()
        player.draw()
        ground.draw()
        forge.update()