from aerforge import *
from aerforge.prefabs import *

class ExitButton():
    def __init__(self, window):
        self.window = window

        self.button = Button(window = self.window, x = self.window.width - 50, y = 0, width = 50, height = 25, color = color.Color(0, 0, 0), highlight_color = color.Color(200, 0, 0), press_color = color.Color(100, 0, 0))
        self.text = Text(self.window, text = "X", x = self.button.x + 20, y = self.button.y + 5)

    def update(self):
        self.button.update()
        
        if self.button.is_pressed():
            self.window.destroy()

    def draw(self):
        self.button.draw()
        self.text.draw()