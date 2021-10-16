from aerforge import *

class TextBox:
    def __init__(self, window, shape = Rect, background_color = (0, 240, 255), background_focus_color = (0, 140, 255), foreground_color = Color(240, 240, 240), foreground_focus_color = Color(240, 240, 240), text_color = Color(40, 40, 40), text_focus_color = Color(40, 40, 40), font_size = 24, font_file = None, text_x = 0, text_y = 0, background_thickness = 2, text_size_limit = 16, x = 0, y = 0, width = 200, height = 50):
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

        self.background_thickness = background_thickness

        self.text_size_limit = text_size_limit
        self.background_color = background_color
        self.background_focus_color = background_focus_color
        self.foreground_color = foreground_color
        self.foreground_focus_color = foreground_focus_color
        self.text_color = text_color
        self.text_focus_color = text_focus_color

        self.font_size = font_size
        self.font_file = font_file

        self.background = GameObject(self.window, shape = shape, color = self.background_color, width = self.width, height = self.height, x = self.x, y = self.y)
        self.foreground = GameObject(self.window, shape = shape, color = self.foreground_color, width = self.width - self.background_thickness * 2, height = self.height - self.background_thickness * 2, x = self.x + self.background_thickness, y = self.y + self.background_thickness)
        self.text_renderer = Text(self.window, text = self.text, font_file = self.font_file, font_size = self.font_size, color = self.text_color, x = self.x + 15 + self.text_x, y = self.y + (self.foreground.height / 2) + (self.font_size / 3) + self.text_y)

    def draw(self):
        self.background.draw()
        self.foreground.draw()
        self.text_renderer.draw()

    def center(self):
        self.x = self.window.width / 2 - self.width / 2
        self.y = self.window.height / 2 - self.height / 2

    def center_x(self):
        self.x = self.window.width / 2 - self.width / 2

    def center_y(self):
        self.y = self.window.height / 2 - self.height / 2

    def hit(self, gameobject):
        return self.background.hit(gameobject)

    def destroy(self):
        self.background.destroy()
        self.foreground.destroy()
        self.text_renderer.destroy()

    def update(self):
        self.background.x, self.background.y = self.x, self.y
        self.background.width, self.background.height = self.width, self.height
        self.foreground.x, self.foreground.y = self.x + self.background_thickness, self.y + self.background_thickness
        self.foreground.width, self.foreground.height = self.width - self.background_thickness * 2, self.height - self.background_thickness * 2
        self.text_renderer.x, self.text_renderer.y = self.x + 15 + self.text_x, self.y + (self.foreground.height / 2) - 5 + self.text_y

        self.text_renderer.text = self.text

        if self.active:
            self.background.color = self.background_focus_color
            self.foreground.color = self.foreground_focus_color
            self.text_renderer.color = self.text_focus_color

            if self.returned:
                self.returned = False
                self.returned_text = ""

            if self.window.input.key_pressed(self.window.keys["RETURN"]):
                if self.return_state:
                    self.returned_text = self.text
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
                        self.text = self.text + self.window.input._pressed_key

        else:
            self.background.color = self.background_color
            self.foreground.color = self.foreground_color
            self.text_renderer.color = self.text_color

        if self.foreground.hit(self.window.input.mouse_pos()):
            if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
                self.active = True

        else:
            if self.window.input.mouse_pressed(self.window.buttons["LEFT"]):
                self.active = False

if __name__ == "__main__":
    forge = Forge()

    text_box = TextBox(forge)
    text_box.center()

    while True:
        if text_box.returned:
            print(text_box.returned_text)

        text_box.update()
        text_box.draw()
        forge.update()