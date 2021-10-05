from aerforge import *

class Gravity:
    def __init__(self, object, gravity = 0.6):
        self.object = object

        self.objects = []

        self.state = False
        self.grounded = False
        self.velocity = 0

        self.gravity = gravity

    def force(self, force):
        self.velocity = self.velocity + force

    def update(self):
        self.object.y = self.object.y + self.velocity

        self.state = False

        for i in self.objects:
            if not i.destroyed:
                if self.object.hit(i):
                    self.object.y = i.y - self.object.height + 1
                    self.velocity = 0
                    self.grounded = True
                    self.state = True

        if not self.state:
            self.grounded = False

        self.state = False

        if not self.grounded:
            self.velocity = self.velocity + self.gravity

if __name__ == "__main__":
    forge = Forge()

    cube = GameObject(window = forge, shape = Rect, width = 50, height = 50, color = (50, 50, 100))
    cube.center()

    ground = GameObject(window = forge, shape = Rect, width = 1200, height = 50, color = GRAY)
    ground.y = 550

    gravity = Gravity(cube)
    gravity.objects.append(ground)

    while True:
        gravity.update()
        forge.drawall()
        forge.update()