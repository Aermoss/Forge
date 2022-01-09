class Vec3:
    def __init__(self, arg1, arg2 = None, arg3 = None):
        if isinstance(arg1, tuple):
            self.x = arg1[0]
            self.y = arg1[1]
            self.z = arg1[2]

        else:
            self.x = arg1
            self.y = arg2
            self.z = arg3

    def lerp(self, vec3, value):
        self.x = self.x + (vec3.x - self.x) * value
        self.y = self.y + (vec3.y - self.y) * value
        self.z = self.z + (vec3.z - self.z) * value