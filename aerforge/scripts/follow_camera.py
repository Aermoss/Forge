from aerforge import *

class FollowCamera:
    def __init__(self, camera, value = 0.9):
        self.camera = camera
        self.value = value

    def update(self, entity):
        pos = Vec2(self.camera.get_entity_pos(entity).x + entity.width / 2 - self.camera.window.width / 2, self.camera.get_entity_pos(entity).y + entity.height / 2 - self.camera.window.height / 2)
        self.camera.set_pos(pos.x, pos.y)