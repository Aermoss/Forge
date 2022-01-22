from aerforge import *

class FpsCounter(Text):
    def __init__(self, window, font_size = 24, font_file = None, font_name = "arial", color = color.Color(240, 240, 240), x = 0, y = 0, get_integer = True):
        super().__init__(
            text = "",
            window = window,
            font_size = font_size,
            font_file = font_file,
            font_name = font_name,
            color = color,
            x = x,
            y = y,
        )

        self.get_integer = get_integer

    def update(self):
        if self.get_integer:
            self.text = str(int(self.window.get_fps()))
        else:
            self.text = str(self.window.get_fps())