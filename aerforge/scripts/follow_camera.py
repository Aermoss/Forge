class FollowCamera:
    def __init__(self, camera):
        self.camera = camera

    def update(self, entity):
        self.camera.set_pos(self.camera.get_entity_pos(entity)[0] + entity.width / 2 - self.camera.window.width / 2, self.camera.get_entity_pos(entity)[1] + entity.height / 2 - self.camera.window.height / 2)