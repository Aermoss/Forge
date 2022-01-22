from aerforge import *

forge = Forge()

class Cube(Entity):
    def __init__(self):
        super().__init__(
            window = forge,
            shape = shape.Rect,
            width = 20,
            height = 20,
            x = 0,
            y = 0,
            color = color.Color(0, 255, 255)
        )

        self.center()

cube = Cube()

@forge.update
def update(dt):
    pass

forge.run()