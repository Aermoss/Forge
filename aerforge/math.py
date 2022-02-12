from aerforge import color

def lerp(a, b, value):
    if isinstance(a, int) or isinstance(a, float):
        return a + (b - a) * value

    elif isinstance(a, Vec2):
        return Vec3(lerp(a.x, b.x, value), lerp(a.y, b.y, value))

    elif isinstance(a, Vec3):
        return Vec3(lerp(a.x, b.x, value), lerp(a.y, b.y, value), lerp(a.z, b.z, value))

    elif isinstance(a, color.Color):
        return color.Color(lerp(a.r, b.r, value), lerp(a.g, b.g, value), lerp(a.b, b.b, value), lerp(a.a, b.a, value))

class Vec2:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def get(self):
        return (self.x, self.y)

    def __add__(self, value):
        return Vec2(self.x + value.x, self.y + value.y)

    def __sub__(self, value):
        return Vec2(self.x - value.x, self.y - value.y)

    def __mul__(self, value):
        if isinstance(value, (int, float)):
            return Vec2(self.x * value, self.y * value)

        return Vec2(self.x * value.x, self.y * value.y)

    def __truediv__(self, value):
        if isinstance(value, (int, float)):
            return Vec2(self.x / value, self.y / value)

        return Vec2(self.x / value.x, self.y / value.y)
    
    def __repr__(self):
        return str((self.x, self.y))

class Vec3:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def get(self):
        return (self.x, self.y, self.z)

    def __add__(self, value):
        return Vec3(self.x + value.x, self.y + value.y, self.z + value.z)

    def __sub__(self, value):
        return Vec3(self.x - value.x, self.y - value.y, self.z - value.z)

    def __mul__(self, value):
        if isinstance(value, (int, float)):
            return Vec3(self.x * value, self.y * value, self.z * value)

        return Vec3(self.x * value.x, self.y * value.y, self.z * value.z)

    def __truediv__(self, value):
        if isinstance(value, (int, float)):
            return Vec3(self.x / value, self.y / value, self.z / value)

        return Vec3(self.x / value.x, self.y / value.y, self.z / value.z)
    
    def __repr__(self):
        return str((self.x, self.y, self.z))