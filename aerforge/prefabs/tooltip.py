from aerforge import *

class ToolTip(Entity):
    def __init__(self, window, object, shape = shape.Rect, width = 100, height = 50, color = color.Color(5, 5, 5), font_file = None, font_name = "arial", font_size = 24, text = "", text_x = 0, text_y = 0):
        super().__init__(
            window = window, 
            shape = shape, 
            width = width, 
            height = height,  
            x = 0,
            y = 0, 
            color = color,
            add_to_objects = False,
        )

        self.text_x = text_x
        self.text_y = text_y
        self.text = text
        self.font_size = font_size
        self.font_name = font_name
        self.file = font_file

        self.tooltip_text = Text(self.window, font_file = self.file, font_name = font_name, font_size = self.font_size, text = text, add_to_objects = False)

        self.object = object

    def update(self):
        pos = self.window.input.mouse_pos()
        self.x, self.y = pos.x, pos.y
        self.tooltip_text.x, self.tooltip_text.y = self.x + self.width / 2 - self.tooltip_text.get_width() / 2, self.y + self.height / 2 - self.tooltip_text.get_height() / 2
        self.tooltip_text.text = self.text

        if self.object.hit(self.window.input.mouse_pos()):
            self.draw()
            self.tooltip_text.draw()