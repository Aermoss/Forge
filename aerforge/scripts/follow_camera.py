from aerforge import *

class FollowCamera:
    def __init__(self, camera):
        self.camera = camera
        self.pos = math.Vec2(0, 0)

    def update(self, entity):
        self.pos = math.Vec2(self.camera.get_entity_pos(entity).x + entity.width / 2 - self.camera.window.width / 2, self.camera.get_entity_pos(entity).y + entity.height / 2 - self.camera.window.height / 2)
        self.camera.set_pos(self.pos.x, self.pos.y)