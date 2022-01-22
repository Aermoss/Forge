from aerforge import *

class Camera:
    def __init__(self, window):
        self.window = window

        self.movement = (0, 0)
        self.default = (0, 0)

    def _set_pos(self, x, y):
        for i in self.window.objects:
            i.x = i.x - (x - (self.window.width / 2))
            i.y = i.y - (y - (self.window.height / 2))

        self.movement = (((x - (self.window.width / 2))), (y - (self.window.height / 2)))
        self.default = (self.default[0] - self.movement[0], self.default[1] - self.movement[1])

    def set_pos(self, x, y):
        self._set_pos(self.default[0] + x + (self.window.width / 2), self.default[1] + y + (self.window.height / 2))

    def get_pos(self):
        return Vec2(self.default[0], self.default[1])

    def set_entity_pos(self, entity, x, y):
        entity.x = x + self.default[0]
        entity.y = y + self.default[1]

    def get_entity_pos(self, entity):
        return Vec2(entity.x - self.default[0], entity.y - self.default[1])