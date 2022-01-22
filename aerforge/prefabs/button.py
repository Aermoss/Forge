from aerforge import *

class Button(Entity):
    def __init__(self, window,
        shape = shape.Rect,
        width = 300,
        height = 100,
        x = 0,
        y = 0,
        color = color.Color(30, 30, 30),
        highlight_color = color.Color(240, 240, 240),
        press_color = color.Color(10, 10, 10),
        frame = True,
        frame_color = color.Color(240, 240, 240),
        normal_color_lerp = 0.6,
        highlight_color_lerp = 0.6,
        press_color_lerp = 0.1,
        text = "",
        font_size = 24,
        font_file = None,
        font_name = "arial",
        text_color = color.Color(240, 240, 240),
        text_highlight_color = color.Color(10, 10, 10),
        text_normal_color_lerp = 0.6,
        text_highlight_color_lerp = 0.6
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

        self.text = text
        self.font_size = font_size
        self.font_file = font_file
        self.font_name = font_name
        self.text_normal_color = text_color
        self.text_highlight_color = text_highlight_color

        self.text_normal_color_lerp = text_normal_color_lerp
        self.text_highlight_color_lerp = text_highlight_color_lerp

        self.text_renderer = Text(self.window, self.text, self.font_size, self.font_file, self.font_name, self.text_normal_color)

        self.normal_color = color
        self.highlight_color = highlight_color
        self.press_color = press_color

        self.state = False
        self.pressed = False
        self.highlight = False

        self.normal_color_lerp = normal_color_lerp
        self.highlight_color_lerp = highlight_color_lerp
        self.press_color_lerp = press_color_lerp

        self.frame = frame
        self.frame_color = frame_color

        if self.frame:
            self.frame = Entity(window, shape = shape, width = width, height = height, x = x, y = y, color = self.frame_color, fill = False)

    def update(self):
        if self.text != "":
            self.text_renderer.text = self.text
            self.text_renderer.font_size = self.font_size
            self.text_renderer.font_file = self.font_file

            if self.pressed or self.highlight:
                self.set_color(self.text_renderer, self.text_highlight_color, self.text_highlight_color_lerp)

            else:
                self.set_color(self.text_renderer, self.text_normal_color, self.text_normal_color_lerp)

            text = self.text_renderer.font.render(self.text_renderer.text, True, self.text_renderer.color)
            self.text_renderer.x, self.text_renderer.y = self.x + self.width / 2 - text.get_width() / 2, self.y + self.height / 2 - text.get_height() / 2

        if self.frame:
            self.frame.shape, self.frame.x, self.frame.y, self.frame.width, self.frame.height, self.frame.color = self.shape, self.x, self.y, self.width, self.height, self.frame_color

        if self.pressed:
            self.pressed = False

        if self.highlight:
            self.highlight = False

        if self.hit(self.window.input.mouse_pos()):
            if self.window.is_mouse_focused():
                self.highlight = True

            if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
                if self.state:
                    self.state = False
                    self.pressed = True
            else:
                self.state = True
        else:
            self.state = True

        if self.pressed:
            self.highlight = False

        if self.highlight:
            self.set_color(self, self.highlight_color, self.highlight_color_lerp)

        elif self.pressed:
            self.set_color(self, self.press_color, self.press_color_lerp)

        else:
            self.set_color(self, self.normal_color, self.normal_color_lerp)

    def set_color(self, object, target_color, value):
        active_color = Vec3(object.color.r, object.color.g, object.color.b)
        active_color.lerp(Vec3(target_color.r, target_color.g, target_color.b), value)
        object.color = color.Color(int(active_color.x), int(active_color.y), int(active_color.z))

    def drawall(self):
        self.draw()

        if self.frame:
            self.frame.draw()

        if self.text != "":
            self.text_renderer.draw()

    def destroyall(self):
        self.destroy()
        self.frame.destroy()
        self.text_renderer.destroy()

    def is_pressed(self):
        if self.pressed:
            return True

        return False