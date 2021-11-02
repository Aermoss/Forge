from aerforge import *

class Cursor(Entity):
    def __init__(self, window, shape = Circle, width = 10, height = 10):
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
        mouse_x, mouse_y = self.window.input.mouse_pos()
        self.x, self.y = mouse_x - self.width / 2, mouse_y - self.height / 2

if __name__ == "__main__":
    from aerforge.prefabs import *

    forge = Forge()

    cursor = Cursor(forge)

    while True:
        cursor.update()
        cursor.draw()
        forge.update()