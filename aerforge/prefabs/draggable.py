from aerforge import *

class Draggable:
    def __init__(self, window, object, center = False):
        self.window = window
        self.object = object

        self.center = center

        self.grab_pos = (0, 0)

    def update(self):
        if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
            if self.object.hit(self.window.input.mouse_pos()):
                if not self.state:
                    mouse_x, mouse_y = self.window.input.mouse_pos()
                    self.grab_pos = (self.object.x - mouse_x, self.object.y - mouse_y)

                self.state = True

        else:
            self.state = False

        if self.state:
            mouse_x, mouse_y = self.window.input.mouse_pos()

            if self.center:
                self.object.x, self.object.y = (mouse_x - (self.object.width / 2), mouse_y - (self.object.height / 2))

            else:
                self.object.x, self.object.y = (mouse_x + self.grab_pos[0], mouse_y + self.grab_pos[1])

if __name__ == "__main__":
    from aerforge.prefabs import *

    forge = Forge()

    cube = GameObject(forge, shape = Rect, width = 200, height = 200)
    cube.center()

    draggable = Draggable(forge, cube, True)

    while True:
        cube.draw()
        draggable.update()
        forge.update()