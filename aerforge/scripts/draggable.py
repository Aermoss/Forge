from aerforge import *

class Draggable:
    def __init__(self, window, center = False):
        self.window = window
        self.center = center

        self.grab_start = (0, 0)
        self.grab = False
        self.state = True

    def update(self, entity):
        if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
            if self.state:
                self.state = False

                if entity.hit(self.window.input.mouse_pos()):
                    self.grab = True
                    self.grab_start = (entity.x - self.window.input.mouse_pos().x, entity.y - self.window.input.mouse_pos().y)

        else:
            self.grab_start = (0, 0)
            self.grab = False
            self.state = True

        if self.grab:
            mouse = self.window.input.mouse_pos()

            if self.center:
                entity.x, entity.y = (mouse.x - (entity.width / 2), mouse.y - (entity.height / 2))

            else:
                entity.x, entity.y = (mouse.x + self.grab_start[0], mouse.y + self.grab_start[1])

if __name__ == "__main__":
    from aerforge import *

    forge = Forge()

    entity = Entity(forge)
    entity.center()

    entity.add_script(Draggable(forge))

    forge.run()