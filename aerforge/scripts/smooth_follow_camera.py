from aerforge import *

class SmoothFollowCamera:
    def __init__(self, camera, value = 0.9):
        self.camera = camera
        self.value = value

        self.pos = Vec2(0, 0)

    def update(self, entity):
        self.pos.lerp(Vec2(self.camera.get_entity_pos(entity).x + entity.width / 2 - self.camera.window.width / 2, self.camera.get_entity_pos(entity).y + entity.height / 2 - self.camera.window.height / 2), self.value)
        self.camera.set_pos(self.pos.x, self.pos.y)