from aerforge import *

forge = Forge()

class Cube(GameObject):
    def __init__(self):
        super().__init__(
            window = forge,
            shape = Rect,
            width = 20,
            height = 20,
            x = 0,
            y = 0,
            color = (0, 255, 255)
        )

        self.center()

cube = Cube()

while True:
    forge.drawall()
    forge.update()