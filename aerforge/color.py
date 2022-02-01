class Color:
    def __init__(self, r, g, b, a = 255):
        self.r, self.g, self.b, self.a = r, g, b, a

    def get(self):
        return (self.r, self.g, self.b, self.a)
        
Red = Color(240, 0, 0)
Green = Color(0, 240, 0)
Blue = Color(0, 0, 240)
White = Color(240, 240, 240)
Black = Color(40, 40, 40)