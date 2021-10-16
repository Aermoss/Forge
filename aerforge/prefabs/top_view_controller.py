from aerforge import *

class TopViewController(GameObject):
    def __init__(self, window, shape = Rect, x = 0, y = 0, width = 50, height = 100, color = Color(240, 240, 240), sprint_speed = 6, walk_speed = 3, collision_tolreance = 0, not_complete_features = False):
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

        self.hits = []

        self.collision_tolreance = collision_tolreance
        self.not_complete_features = not_complete_features

        self.speed = 0
        self.sprint_speed = sprint_speed
        self.walk_speed = walk_speed

    def update(self):
        self.hits = []

        for i in self.objects:
            self.hits.append(self.hit2(i, self.collision_tolreance))

            if self.hit2(i) == "top":
                self.y = i.y + i.height

            if self.hit2(i) == "bottom":
                self.y = i.y - self.height

            if self.hit2(i) == "left":
                self.x = i.x + i.width

            if self.hit2(i) == "right":
                self.x = i.x - self.width

            if self.not_complete_features:
                if self.hit2(i) == "unknown":
                    if (self.y + (self.height / 2)) < (i.y + (i.height / 2)):
                        self.y = i.y - self.height
                
                    if (self.y + (self.height / 2)) > (i.y + (i.height / 2)):
                        self.y = i.y + i.height
                
                    if (self.x + (self.width / 2)) < (i.x + (i.width / 2)):
                        self.x = i.x - self.width
                
                    if (self.x + (self.width / 2)) > (i.x + (i.width / 2)):
                        self.x = i.x + i.width

        if self.window.input.key_pressed(self.window.keys["LSHIFT"]):
            self.speed = self.sprint_speed
        else:
            self.speed = self.walk_speed

        if self.window.input.key_pressed(self.window.keys["W"]) and "top" not in self.hits:
            self.y = self.y - self.speed

        if self.window.input.key_pressed(self.window.keys["S"]) and "bottom" not in self.hits:
            self.y = self.y + self.speed

        if self.window.input.key_pressed(self.window.keys["A"]) and "left" not in self.hits:
            self.x = self.x - self.speed

        if self.window.input.key_pressed(self.window.keys["D"]) and "right" not in self.hits:
            self.x = self.x + self.speed

if __name__ == "__main__":
    forge = Forge()

    cube = GameObject(forge, Rect, width = 200, height = 200, color = Color(100, 100, 180))
    cube.center()

    player = TopViewController(forge)

    player.objects.append(cube)

    while True:
        cube.draw()
        player.update()
        player.draw()
        forge.update()