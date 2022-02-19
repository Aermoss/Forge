from aerforge import *

class Modifiable:
    def __init__(self, window):
        self.window = window

        self.grab = ""
        self.grab_start = (0, 0)
        self.start_size = (0, 0)
        self.start_pos = (0, 0)
        self.state = True

    def update(self, entity):
        if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
            if self.state:
                self.state = False

                if self.hit_sides(entity):
                    self.grab = self.hit_sides(entity)
                    self.grab_start = (self.window.input.mouse_pos().x, self.window.input.mouse_pos().y)
                    self.start_size = (entity.width, entity.height)
                    self.start_pos = (entity.x, entity.y)

        else:
            self.grab = ""
            self.grab_start = (0, 0)
            self.start_size = (0, 0)
            self.start_pos = (0, 0)
            self.state = True

        if self.grab:
            mouse = self.window.input.mouse_pos()

            if self.grab[1] == "left":
                change = self.grab_start[0] - mouse.x
                entity.width = change + self.start_size[0]
                entity.x = self.start_pos[0] - change

            if self.grab[1] == "right":
                change = self.grab_start[0] - mouse.x
                entity.width = self.start_size[0] - change

            if self.grab[1] == "up":
                change = self.grab_start[1] - mouse.y
                entity.height = change + self.start_size[1]
                entity.y = self.start_pos[1] - change

            if self.grab[1] == "down":
                change = self.grab_start[1] - mouse.y
                entity.height = self.start_size[1] - change

    def hit_sides(self, entity):
        mouse = self.window.input.mouse_pos()

        if entity.x + 5 > mouse.x and entity.x - 5 < mouse.x and entity.y < mouse.y and entity.y + entity.height > mouse.y:
            return True, "left"

        if entity.y + 5 > mouse.y and entity.y - 5 < mouse.y and entity.x < mouse.x and entity.x + entity.width > mouse.x:
            return True, "up"

        if entity.x + entity.width + 5 > mouse.x and entity.x + entity.width - 5 < mouse.x and entity.y < mouse.y and entity.y + entity.height > mouse.y:
            return True, "right"

        if entity.y + entity.height + 5 > mouse.y and entity.y + entity.height - 5 < mouse.y and entity.x < mouse.x and entity.x + entity.width > mouse.x:
            return True, "down"

        return False

if __name__ == "__main__":
    from aerforge import *

    forge = Forge()

    entity = Entity(forge)
    entity.center()

    entity.add_script(Modifiable(forge))

    forge.run()