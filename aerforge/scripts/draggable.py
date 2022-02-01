from aerforge import *

class Draggable:
    def __init__(self, window, center = False):
        self.window = window
        self.center = center

        self.grab_pos = math.Vec2(0, 0)

    def update(self, entity):
        if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
            if entity.hit(self.window.input.mouse_pos()):
                if not self.state:
                    mouse_pos = self.window.input.mouse_pos()
                    self.grab_pos.x, self.grab_pos.y = entity.x - mouse_pos.x, entity.y - mouse_pos.y

                self.state = True

        else:
            self.state = False

        if self.state:
            mouse_pos = self.window.input.mouse_pos()

            if self.center:
                entity.x, entity.y = (mouse_pos.x - (entity.width / 2), mouse_pos.y - (entity.height / 2))

            else:
                entity.x, entity.y = (mouse_pos.x + self.grab_pos.x, mouse_pos.y + self.grab_pos.y)

if __name__ == "__main__":
    from aerforge import *

    forge = Forge()

    entity = Entity(forge)
    entity.center()

    entity.add_script(Draggable(forge))

    forge.run()