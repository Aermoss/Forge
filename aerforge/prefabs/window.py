from aerforge import *
from aerforge.prefabs import *

class Window:
    def __init__(self, window, 
        save_window_size = True,
        noframe = True,
        bar_color = color.Color(0, 0, 0),
        button_color = color.Color(0, 0, 0),
        button_highlight_color = color.Color(30, 30, 30),
        exit_button_highlight_color = color.Color(240, 0, 0),
        button_press_color = color.Color(0, 0, 0),
        exit_button_press_color = color.Color(100, 0, 0),
        frame_color = color.Color(50, 50, 50),
        frame_focus_color = color.Color(40, 40, 40),
        symbol_color = color.Color(255, 255, 255),
        unavailable_symbol_color = color.Color(110, 110, 110),
        title_color = color.Color(255, 255, 255)
    ):

        self.window = window

        self.bar_color = bar_color
        self.button_color = button_color
        self.button_highlight_color = button_highlight_color
        self.exit_button_highlight_color = exit_button_highlight_color
        self.button_press_color = button_press_color
        self.exit_button_press_color = exit_button_press_color
        self.frame_color = frame_color
        self.frame_focus_color = frame_focus_color
        self.symbol_color = symbol_color
        self.unavailable_symbol_color = unavailable_symbol_color
        self.title_color = title_color

        if save_window_size:
            self.window.height = self.window.height + 30

            if not noframe:
                self.window.build_window()

        if noframe:
            self.window.frame = False
            self.window.build_window()

        self.exit_button = Button(self.window, frame = False, width = 46, height = 30, x = self.window.width - 46 * 1, y = 0, color = self.button_color, highlight_color = self.exit_button_highlight_color, press_color = self.exit_button_press_color, normal_color_lerp = 0.89, highlight_color_lerp = 0.6)
        self.maximize_button = Button(self.window, frame = False, width = 46, height = 30, x = self.window.width - 46 * 2, y = 0, color = self.button_color, highlight_color = self.button_highlight_color, press_color = self.button_press_color, normal_color_lerp = 0.89, highlight_color_lerp = 0.6)
        self.minimize_button = Button(self.window, frame = False, width = 46, height = 30, x = self.window.width - 46 * 3, y = 0, color = self.button_color, highlight_color = self.button_highlight_color, press_color = self.button_press_color, normal_color_lerp = 0.89, highlight_color_lerp = 0.6)
        
        self.bar = Entity(self.window, width = self.window.width, height = 30, x = 0, y = 0, color = self.bar_color)
        
        self.frame = Entity(self.window, width = self.window.width, height = self.window.height, x = 0, y = 0, color = self.frame_color, fill = False)
        
        self.exit_symbol = Line(self.window, [((self.window.width - 19, 20), (self.window.width - 29, 10)), ((self.window.width - 19, 10), (self.window.width - 29, 20))], color = self.symbol_color)
        self.maximize_symbol = Line(self.window, [((self.window.width - 64, 20), (self.window.width - 64, 10)), ((self.window.width - 74, 10), (self.window.width - 74, 20)), ((self.window.width - 64, 20), (self.window.width - 74, 20)), ((self.window.width - 64, 10), (self.window.width - 74, 10))], color = self.unavailable_symbol_color)
        self.minimize_symbol = Line(self.window, [((self.window.width - 110, 15), (self.window.width - 120, 15))], color = self.symbol_color)
        
        self.title = Text(self.window, "Forge", font_name = "segoeuisemibold", x = 32, y = 6, font_size = 12, color = self.title_color)

        try:
            self.icon = Sprite(self.window, file = os.path.join(self.window.path, "./assets/icon/icon_white.png"), width = 20, height = 20, x = 6, y = 5)

        except:
            self.icon = Sprite(self.window, file = "icon_white.png", width = 20, height = 20, x = 6, y = 5)

    def draw(self):
        self.exit_button.drawall()
        self.maximize_button.drawall()
        self.minimize_button.drawall()
        self.exit_symbol.draw()
        self.maximize_symbol.draw()
        self.minimize_symbol.draw()
        self.title.draw()
        self.icon.draw()
        self.frame.draw()

    def update(self):
        if self.exit_button.is_pressed():
            self.window.destroy()

        if self.minimize_button.is_pressed():
            self.window.minimize()

        if self.window.is_focused():
            self.frame.color = self.frame_focus_color

        else:
            self.frame.color = self.frame_color

        self.bar.draw()
        self.exit_button.update()
        self.minimize_button.update()