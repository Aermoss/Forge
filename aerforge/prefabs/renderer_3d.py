from aerforge import *
from math import *

class Entity3D:
    def __init__(self, renderer, verts, faces, colors, pos = Vec3(0, 0, 0), rot = Vec2(0, 0)):
        self.verts = verts
        self.faces = faces
        self.colors = colors
        self.pos = pos
        self.rot = rot

        renderer.objects.append(self)

class Cube(Entity3D):
    def __init__(self, renderer, scale = 1, pos = Vec3(0, 0, 0), rot = Vec2(0, 0), color = color.Color(240, 240, 240)):
        super().__init__(
            renderer = renderer,
            verts = [(-1 * scale, -1 * scale, -1 * scale), (1 * scale, -1 * scale, -1 * scale), (1 * scale, 1 * scale, -1 * scale), (-1 * scale, 1 * scale, -1 * scale), (-1 * scale, -1 * scale, 1 * scale), (1 * scale, -1 * scale, 1 * scale), (1 * scale, 1 * scale, 1 * scale), (-1 * scale, 1 * scale, 1 * scale)],
            faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)],
            colors = [],
            pos = pos,
            rot = rot
        )

        for i in self.faces:
            self.colors.append(color)

class Camera:
    def __init__(self, window, pos = Vec3(0, 0, 0), rot = Vec2(0, 0)):
        self.window = window

        self.pos = pos
        self.rot = rot

        self.speed_normal = 0.05
        self.speed_sprint = 0.10
        self.speed = 0
        self.mouse_sensivity = 1

        self.window.set_mouse_visible(False)
        self.window.set_mouse_lock(True)

    def update_rot(self, x, y):
        x, y = (x * self.mouse_sensivity, y * self.mouse_sensivity)
        x, y = x / (self.window.width / 2), y / (self.window.width / 2)

        self.rot.x = self.rot.x + y
        self.rot.y = self.rot.y + x

        if self.rot.x < -1.5:
            self.rot.x = -1.5

        if self.rot.x > 1.5:
            self.rot.x = 1.5

    def update_pos(self):
        if self.window.input.key_pressed(self.window.keys["LCTRL"]):
            self.speed = self.speed_sprint
        
        else:
            self.speed = self.speed_normal

        if self.window.input.key_pressed(self.window.keys["SPACE"]):
            self.pos.y = self.pos.y - 0.05

        if self.window.input.key_pressed(self.window.keys["LSHIFT"]):
            self.pos.y = self.pos.y + 0.05

        x, y = self.speed * sin(self.rot.y), self.speed * cos(self.rot.y)

        if self.window.input.key_pressed(self.window.keys["W"]):
            self.pos.x = self.pos.x + x
            self.pos.z = self.pos.z + y

        if self.window.input.key_pressed(self.window.keys["S"]):
            self.pos.x = self.pos.x - x
            self.pos.z = self.pos.z - y

        if self.window.input.key_pressed(self.window.keys["A"]):
            self.pos.x = self.pos.x - y
            self.pos.z = self.pos.z + x

        if self.window.input.key_pressed(self.window.keys["D"]):
            self.pos.x = self.pos.x + y
            self.pos.z = self.pos.z - x

class Renderer3D:
    def __init__(self, window, fov = 90, camera_pos = Vec3(0, 0, 0)):
        self.window = window
        self.camera = Camera(self.window, camera_pos)

        self.objects = []

        self.clipping = 1
        self.fov = fov / 180 * pi
        self.proj_y = (self.window.height / 2) / tan(self.fov / 2)
        self.proj_x = (self.window.width / 2) / tan(self.fov / 2) / (self.window.width / self.window.height)

    def update(self):
        x, y = self.window.input.mouse_rel()

        self.camera.update_rot(x, y)
        self.camera.update_pos()

    def load_test_scene(self):
        self.camera.pos.z = -5
        self.objects.append(Cube(self, color = color.Color(240, 50, 50), pos = Vec3(5, 0, 0)))
        self.objects.append(Cube(self, color = color.Color(50, 240, 50), pos = Vec3(0, 5, 0)))
        self.objects.append(Cube(self, color = color.Color(50, 50, 240), pos = Vec3(0, 0, 5)))

    def set_fov(self, fov):
        self.fov = fov / 180 * pi
        self.proj_y = (self.window.height / 2) / tan(self.fov / 2)
        self.proj_x = (self.window.width / 2) / tan(self.fov / 2) / (self.window.width / self.window.height)
            
    def rotate2d(self, pos, rad):
        x, y = pos
        s, c = sin(rad), cos(rad)

        return x * c - y * s, y * c + x * s

    def get2d(self, v):
        return (self.window.width / 2) + int(v[0] / v[2] * self.proj_x), (self.window.height / 2) + int(v[1] / v[2] * self.proj_y)
 
    def get3d(self, v, pos, rot):
        v = (pos.x + v[0] / 2, pos.y + v[1] / 2, pos.z + v[2] / 2)
        x, y, z = v[0] - self.camera.pos.x, v[1] - self.camera.pos.y, v[2] - self.camera.pos.z
        x, z = self.rotate2d((x, z), self.camera.rot.y)
        y, z = self.rotate2d((y, z), self.camera.rot.x)

        return x, y, z
    
    def get_z(self, a, b, new_z):
        if b[2] == a[2] or new_z < a[2] or new_z > b[2]:
            return None

        dx, dy, dz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
        i = (new_z - a[2]) / dz

        return a[0] + dx * i, a[1] + dy * i, new_z

    def draw(self):
        face_list = []
        face_color = []
        depth = []

        for obj in self.objects:
            vert_list = [self.get3d(v, obj.pos, obj.rot) for v in obj.verts]
 
            for f in range(len(obj.faces)):
                verts = [vert_list[i] for i in obj.faces[f]]
 
                i = 0

                while i < len(verts):
                    if verts[i][2] < self.clipping:
                        sides = []

                        l = verts[i - 1]
                        r = verts[(i + 1) % len(verts)]

                        if l[2] > self.clipping:
                            sides = sides + [self.get_z(verts[i], l, self.clipping)]

                        if r[2] > self.clipping:
                            sides = sides + [self.get_z(verts[i], r, self.clipping)]

                        verts = verts[:i] + sides + verts[i + 1:]
                        i = i + len(sides) - 1

                    i = i + 1
 
                if len(verts)>2:
                    face_list = face_list + [[self.get2d(v) for v in verts]]
                    face_color = face_color + [obj.colors[f]]
                    depth = depth + [sum(sum(v[i] / len(verts) for v in verts) ** 2 for i in range(3))]
 
        order = sorted(range(len(face_list)), key = lambda i: depth[i], reverse = 1)

        for i in order:
            try:
                self.window.draw(shape = shape.Polygon, color = face_color[i], points = face_list[i])

            except:
                pass