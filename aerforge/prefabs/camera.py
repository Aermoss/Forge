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

if __name__ == "__main__":
    from aerforge.prefabs import TopViewController

    forge = Forge()

    cube1 = Entity(forge, width = 100, height = 100, x = 100, y = 200)
    cube2 = Entity(forge, width = 100, height = 100, x = 500, y = 300)

    player = TopViewController(forge)

    camera = Camera(forge)

    while True:
        camera.set_pos(camera.get_entity_pos(player).x + player.width / 2 - forge.width / 2, camera.get_entity_pos(player).y + player.height / 2 - forge.height / 2)
        cube1.draw()
        cube2.draw()
        player.update()
        player.draw()
        forge.update()