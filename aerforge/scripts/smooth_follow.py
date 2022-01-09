from aerforge import *

class SmoothFollow:
    def __init__(self, entity, value = 0.1):
        self.entity = entity
        self.value = value

    def update(self, entity):
        entity.x = math.lerp(entity.x, self.entity.x, self.value)
        entity.y = math.lerp(entity.y, self.entity.y, self.value)