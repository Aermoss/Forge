class Vec2:
    def __init__(self, arg1, arg2 = None):
        if isinstance(arg1, tuple):
            self.x = arg1[0]
            self.y = arg1[1]

        else:
            self.x = arg1
            self.y = arg2