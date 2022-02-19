from aerforge import *

class Camera:
    def __init__(self, window):
        self.window = window
        self.pos = math.Vec2(0, 0)
        self.ignored_entitys = []

    def set_pos(self, x, y):
        x, y = int(x), int(y)

        for i in self.window.objects:
            if i not in self.ignored_entitys:
                i.x += self.pos.x
                i.y += self.pos.y

        for i in self.window.objects:
            if i not in self.ignored_entitys:
                i.x -= x
                i.y -= y

        self.pos.x = x
        self.pos.y = y

    def get_pos(self):
        return self.pos

    def get_entity_pos(self, entity):
        return math.Vec2(self.pos.x + entity.x, self.pos.y + entity.y)

    def set_entity_pos(self, entity, x, y):
        entity.x, entity.y = x - self.pos.x, y - self.pos.y

    def ignore(self, entity):
        self.ignored_entitys.append(entity)