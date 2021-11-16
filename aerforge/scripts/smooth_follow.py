from aerforge import *

class SmoothFollow:
    def __init__(self, entity, value = 0.1):
        self.entity = entity
        self.value = value

    def update(self, entity):
        entity_pos = Vec2(self.entity.x, self.entity.y)
        entity_pos.lerp(Vec2(entity.x, entity.y), self.value)
        entity.x, entity.y = entity_pos.x, entity_pos.y