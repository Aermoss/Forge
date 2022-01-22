from aerforge import *

class Draggable:
    def __init__(self, window, object, center = False):
        self.window = window
        self.object = object

        self.center = center

        self.grab_pos = Vec2(0, 0)

    def update(self):
        if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
            if self.object.hit(self.window.input.mouse_pos()):
                if not self.state:
                    mouse_pos = self.window.input.mouse_pos()
                    self.grab_pos.x, self.grab_pos.y = self.object.x - mouse_pos.x, self.object.y - mouse_pos.y

                self.state = True

        else:
            self.state = False

        if self.state:
            mouse_pos = self.window.input.mouse_pos()

            if self.center:
                self.object.x, self.object.y = (mouse_pos.x - (self.object.width / 2), mouse_pos.y - (self.object.height / 2))

            else:
                self.object.x, self.object.y = (mouse_pos.x + self.grab_pos.x, mouse_pos.y + self.grab_pos.y)