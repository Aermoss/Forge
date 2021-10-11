from aerforge import *
from math import *

class Camera:
    def __init__(self, window, pos = (0, 0, 0), rot = (0, 0)):
        self.window = window

        self.pos = list(pos)
        self.rot = list(rot)

        self.speed_normal = 0.05
        self.speed_sprint = 0.10
        self.speed = 0
        self.mouse_sensivity = 1

        self.window.set_mouse_visible(False)
        self.window.set_mouse_lock(True)

    def update_rot(self, x, y):
        x, y = (x * self.mouse_sensivity, y * self.mouse_sensivity)
        x, y = x / (self.window.width / 2), y / (self.window.width / 2)

        self.rot[0] = self.rot[0] + y
        self.rot[1] = self.rot[1] + x

        if self.rot[0] < -1.5:
            self.rot[0] = -1.5

        if self.rot[0] > 1.5:
            self.rot[0] = 1.5

    def update_pos(self):
        if self.window.input.key_pressed(self.window.keys["LCTRL"]):
            self.speed = self.speed_sprint
        
        else:
            self.speed = self.speed_normal

        if self.window.input.key_pressed(self.window.keys["SPACE"]):
            self.pos[1] = self.pos[1] - self.speed

        if self.window.input.key_pressed(self.window.keys["LSHIFT"]):
            self.pos[1] = self.pos[1] + self.speed

        x, y = self.speed * sin(self.rot[1]), self.speed * cos(self.rot[1])

        if self.window.input.key_pressed(self.window.keys["W"]):
            self.pos[0] = self.pos[0] + x
            self.pos[2] = self.pos[2] + y

        if self.window.input.key_pressed(self.window.keys["S"]):
            self.pos[0] = self.pos[0] - x
            self.pos[2] = self.pos[2] - y

        if self.window.input.key_pressed(self.window.keys["A"]):
            self.pos[0] = self.pos[0] - y
            self.pos[2] = self.pos[2] + x

        if self.window.input.key_pressed(self.window.keys["D"]):
            self.pos[0] = self.pos[0] + y
            self.pos[2] = self.pos[2] - x

class Renderer3D:
    def __init__(self, window, camera_pos = (0, 0, -5)):
        self.window = window
        self.camera = Camera(self.window, camera_pos)

        self.objects = []

    def update(self):
        x, y = self.window.input.mouse_rel()

        self.camera.update_rot(x, y)
        self.camera.update_pos()
            
    def rotate2d(self, pos, rad):
        x, y = pos
        s, c = sin(rad), cos(rad)

        return x * c - y * s, y * c + x * s

    def render(self):
        face_list = []
        face_color = []
        depth = []

        for obj in self.objects:
            vert_list = []
            screen_coords = []

            for x, y, z in obj.verts:
                x = x - self.camera.pos[0]
                y = y - self.camera.pos[1]
                z = z - self.camera.pos[2]

                print()

                x, z = self.rotate2d((x, z), self.camera.rot[1])
                y, z = self.rotate2d((y, z), self.camera.rot[0])

                vert_list.append((x, y, z))

                f = (self.window.width / 2) / z
                x, y = x * f, y * f

                screen_coords.append(((self.window.width / 2) + int(x), (self.window.height / 2) + int(y)))

            for f in range(len(obj.faces)):
                face = obj.faces[f]

                on_screen = False

                for i in face:
                    x, y = screen_coords[i]

                    if vert_list[i][2] > 0 and x > 0 and x < self.window.width and y > 0 and y < self.window.height:
                        on_screen = True
                        break

                if on_screen:
                    coords = []

                    for i in face:
                        coords.append(screen_coords[i])
                    face_list.append(coords)

                    face_color.append(obj.colors[f])
                    depth.append(sum(sum(vert_list[j][i] for j in face) ** 2 for i in range(3)))

        order = sorted(range(len(face_list)), key = lambda i: depth[i], reverse = True)

        for i in order:
            try:
                self.window.draw(Polygon, color = face_color[i], points = face_list[i])
            
            except:
                pass