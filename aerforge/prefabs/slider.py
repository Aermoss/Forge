from aerforge import *

class Head(Entity):
    def __init__(self, window,
        min = 0,
        max = 200,
        shape = shape.Rect,
        width = 20,
        height = 50,
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

        self.normal_color = color
        self.highlight_color = highlight_color
        self.press_color = press_color

        self.state = False
        self.slide_state = False
        self.pressed = False
        self.highlight = False

        self.active_color = Vec3(color.r, color.g, color.b)

        self.normal_color_lerp = normal_color_lerp
        self.highlight_color_lerp = highlight_color_lerp
        self.press_color_lerp = press_color_lerp

        self.min = min
        self.max = max

        self.value = 0

        self.grab_pos = Vec2(0, 0)

        self.frame = frame
        self.frame_color = frame_color

        if self.frame:
            self.frame = Entity(window, shape = shape, width = width, height = height, x = x, y = y, color = self.frame_color, fill = False)

    def update(self):
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

        if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
            if self.hit(self.window.input.mouse_pos()):
                if not self.slide_state:
                    mouse_pos = self.window.input.mouse_pos()
                    self.grab_pos.x, self.grab_pos.y = self.x - mouse_pos.x, self.y - mouse_pos.y

                self.slide_state = True

        else:
            self.slide_state = False

        if self.slide_state:
            self.x = self.window.input.mouse_pos().x + self.grab_pos.x

        if self.x > self.max:
            self.x = self.max

        if self.x < self.min:
            self.x = self.min

        self.value = self.x - self.min

    def set_color(self, object, target_color, value):
        active_color = Vec3(object.color.r, object.color.g, object.color.b)
        active_color.lerp(Vec3(target_color.r, target_color.g, target_color.b), value)
        object.color = color.Color(int(active_color.x), int(active_color.y), int(active_color.z))

    def drawall(self):
        self.draw()

        if self.frame:
            self.frame.draw()

    def destroyall(self):
        self.destroy()
        self.frame.destroy()

class Slider(Entity):
    def __init__(self, window,
        shape = shape.Rect,
        width = 20,
        height = 50,
        x = 0,
        y = 0,
        min = 0,
        max = 200,
        base_width = 220,
        base_height = 10,
        color = color.Color(30, 30, 30),
        highlight_color = color.Color(240, 240, 240),
        press_color = color.Color(10, 10, 10),
        frame = True,
        frame_color = color.Color(240, 240, 240),
        normal_color_lerp = 0.6,
        highlight_color_lerp = 0.6,
        press_color_lerp = 0.1,
    ):

        super().__init__(
            window = window, 
            shape = shape, 
            width = base_width, 
            height = base_height,  
            x = x, 
            y = y,
            color = color,
        )

        self.min = min
        self.max = max

        self.value = 0

        self.head = Head(window, x + min, x + max, shape, width, height, x, y, color, highlight_color, press_color, frame, frame_color, normal_color_lerp, highlight_color_lerp, press_color_lerp)
        
    def update(self):
        self.head.y = self.y - self.head.height / 2 + self.height / 2
        self.head.min = self.x + self.min
        self.head.max = self.x + self.max
        self.head.update()
        self.value = self.head.value

    def drawall(self):
        self.draw()
        self.head.drawall()

    def get_value(self):
        return self.value