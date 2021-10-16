from aerforge import *

class Camera:
    def __init__(self, window):
        self.window = window

    def set_pos(self, x, y):
        for i in self.window.objects:
            i.x = i.x - (x - self.window.width / 2)
            i.y = i.y - (y - self.window.height / 2)

if __name__ == "__main__":
    from aerforge.prefabs import *

    forge = Forge()

    cube1 = GameObject(forge, width = 100, height = 100, x = 100, y = 200)
    cube2 = GameObject(forge, width = 100, height = 100, x = 500, y = 300)

    player = TopViewController(forge)

    camera = Camera(forge)

    while True:
        camera.set_pos(player.x + player.width / 2, player.y + player.height / 2)
        cube1.draw()
        cube2.draw()
        player.update()
        player.draw()
        forge.update()