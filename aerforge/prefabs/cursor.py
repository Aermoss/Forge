from aerforge import *

class Cursor(Entity):
    def __init__(self, window, shape = shape.Circle, width = 10, height = 10):
        super().__init__(
            window = window,
            shape = shape,
            width = width,
            height = height,
            x = 0,
            y = 0,
        )

        self.window.set_mouse_visible(False)

    def update(self):
        self.x, self.y = self.window.input.mouse_pos().x - self.width / 2, self.window.input.mouse_pos().y - self.height / 2