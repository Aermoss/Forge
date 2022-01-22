from aerforge import *

class TextBox(Entity):
    def __init__(self, window,
        shape = shape.Rect,
        color = color.Color(30, 30, 30),
        highlight_color = color.Color(240, 240, 240),
        frame_color = color.Color(240, 240, 240),
        frame_highlight_color = color.Color(240, 240, 240),
        text_color = color.Color(10, 10, 10),
        text_highlight_color = color.Color(240, 240, 240),
        font_size = 24,
        font_file = None,
        font_name = "arial",
        text_x = 0,
        text_y = 0,
        text_size_limit = 16,
        x = 0,
        y = 0,
        width = 200,
        height = 50
    ):

        super().__init__(
            window = window,
            shape = shape,
            width = width,
            height = height,
            x = x,
            y = y,
            color = color,
        )

        self.window = window
        
        self.text = ""
        self.returned_text = ""

        self.active = False
        self.backspace_state = False
        self.return_state = False
        self.returned = False

        self.text_x = text_x
        self.text_y = text_y

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.text_size_limit = text_size_limit
        self.normal_color = color
        self.highlight_color = highlight_color
        self.frame_color = frame_color
        self.frame_highlight_color = frame_highlight_color
        self.text_color = text_color
        self.text_highlight_color = text_highlight_color

        self.font_size = font_size
        self.font_file = font_file
        self.font_name = font_name

        self.frame = Entity(self.window, shape = shape, color = self.frame_color, width = self.width, height = self.height, x = x, y = y, fill = False)
        self.text_renderer = Text(self.window, text = self.text, font_file = self.font_file, font_name = self.font_name, font_size = self.font_size, color = self.text_color, x = x, y = y)

    def update(self):
        self.frame.x, self.frame.y = self.x, self.y
        self.frame.width, self.frame.height = self.width, self.height
        text = self.text_renderer.font.render(self.text_renderer.text, True, self.text_renderer.color)
        self.text_renderer.x, self.text_renderer.y = self.x + self.width / 2 - text.get_width() / 2, self.y + self.height / 2 - text.get_height() / 2

        self.text_renderer.text = self.text

        if self.active:
            self.set_color(self.frame, self.frame_highlight_color, 0.6)
            self.set_color(self, self.highlight_color, 0.6)
            self.set_color(self.text_renderer, self.text_color, 0.6)

            if self.returned:
                self.returned = False
                self.returned_text = ""

            if self.window.input.key_pressed(self.window.keys["RETURN"]):
                if self.return_state:
                    self.returned_text = self.text[:-1]
                    self.text = ""
                    self.returned = True
                    self.return_state = False

            else:
                self.return_state = True

            if self.window.input.key_pressed(self.window.keys["BACKSPACE"]):
                if self.backspace_state:
                    self.text = self.text[:-2]
                    self.backspace_state = False
            
            else:
                self.backspace_state = True

                if self.window.input.key_pressed():
                    if len(self.text) < self.text_size_limit:
                        self.text += self.window.input.key_name()

        else:
            self.set_color(self.frame, self.frame_color, 0.6)
            self.set_color(self, self.normal_color, 0.6)
            self.set_color(self.text_renderer, self.text_highlight_color, 0.6)

        if self.hit(self.window.input.mouse_pos()):
            if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
                self.active = True

        else:
            if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
                self.active = False

    def set_color(self, object, target_color, value):
        active_color = Vec3(object.color.r, object.color.g, object.color.b)
        active_color.lerp(Vec3(target_color.r, target_color.g, target_color.b), value)
        object.color = color.Color(int(active_color.x), int(active_color.y), int(active_color.z))

    def drawall(self):
        self.draw()
        self.frame.draw()
        self.text_renderer.draw()

    def destroyall(self):
        self.destroy()
        self.frame.destroy()
        self.text_renderer.destroy()

    def is_returned(self):
        if self.returned:
            return True

        return False

    def get_returned(self):
        return self.returned_text