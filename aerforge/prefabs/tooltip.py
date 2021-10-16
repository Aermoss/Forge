from aerforge import *

class ToolTip(GameObject):
    def __init__(self, window, object, shape = Rect, width = 100, height = 50, color = (5, 5, 5), file = None, size = 24, text = "", text_x = 0, text_y = 0):
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
        self.size = size
        self.file = file

        self.tooltip_text = Text(self.window, font_file = self.file, font_size = self.size, text = text, add_to_objects = False)

        self.object = object

    def update(self):
        self.x, self.y = self.window.input.mouse_pos()
        self.tooltip_text.x, self.tooltip_text.y = self.x + 15 + self.text_x, self.y + (self.height / 2) - (self.size / 3) + self.text_y
        self.tooltip_text.text = self.text

        if self.object.hit(self.window.input.mouse_pos()):
            self.draw()
            self.tooltip_text.draw()

if __name__ == "__main__":
    forge = Forge()

    game_object = GameObject(forge, shape = Rect)
    game_object.center()

    tooltip = ToolTip(forge, game_object, shape = Rect, text = "Sword", width = 150, height = 50, size = 30)

    while True:
        game_object.draw()
        tooltip.update()
        forge.update()