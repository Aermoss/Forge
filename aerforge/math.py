from aerforge import color

def lerp(a, b, t):
    if isinstance(a, int) or isinstance(a, float):
        return a + (b - a) * t

    elif isinstance(a, Vec2):
        return Vec3(lerp(a.x, b.x, t), lerp(a.y, b.y, t))

    elif isinstance(a, Vec3):
        return Vec3(lerp(a.x, b.x, t), lerp(a.y, b.y, t), lerp(a.z, b.z, t))

    elif isinstance(a, color.Color):
        return color.Color(lerp(a.r, b.r, t), lerp(a.g, b.g, t), lerp(a.b, b.b, t), lerp(a.a, b.a, t))

class Vec2:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def get(self):
        return (self.x, self.y)

class Vec3:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def get(self):
        return (self.x, self.y, self.z)