from aerforge import *

class HealthBar:
    def __init__(self, window, health = 100, x = 0, y = 0):
        self.window = window
        self.health = health

        self.x = x
        self.y = y

        self.health_bar = Entity(self.window, width = self.health, height = 20, x = self.x + 5, y = self.y + 5, color = color.Color(10, 220, 10), alpha = 200)
        self.health_bar_background = Entity(self.window, width = self.health + 10, height = 30, x = self.x, y = self.y, color = color.Color(40, 40, 40), alpha = 120)

    def set_health(self, health):
        if health < 0:
            health = 0
            
        self.health = health
        self.health_bar.width = self.health

    def get_health(self):
        return self.health

    def set_x(self, x):
        self.x = x
        self.health_bar.x = self.x + 5
        self.health_bar_background.x = self.x

    def set_y(self, y):
        self.y = y
        self.health_bar.y = self.y + 5
        self.health_bar_background.y = self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self):
        self.health_bar.draw()
        self.health_bar_background.draw()