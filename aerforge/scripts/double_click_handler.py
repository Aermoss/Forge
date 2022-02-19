from aerforge import *

import time

class DoubleClickHandler:
    def __init__(self, window, handler, key, time = 0.20, over = True):
        self.window = window
        self.handler = handler
        self.key = key
        self.time = time
        self.over = over

        self.last = 0
        self.state = False

    def update(self, entity):
        if self.key in self.window.buttons.values():
            if self.window.input.mouse_pressed(self.key):
                if self.state:
                    self.state = False

                    if entity.hit(self.window.input.mouse_pos()) or not self.over:
                        if self.last + self.time > time.time():
                            self.handler(entity)

                        self.last = time.time()

            else:
                self.state = True

        if self.key in self.window.keys.values():
            if self.window.input.key_pressed(self.key):
                if self.state:
                    self.state = False

                    if entity.hit(self.window.input.mouse_pos()) or not self.over:
                        if self.last + self.time > time.time():
                            self.handler(entity)

                        self.last = time.time()

            else:
                self.state = True

if __name__ == "__main__":
    from aerforge import *

    forge = Forge()

    entity = Entity(forge)
    entity.center()

    def handler(entity):
        print("Double click")
    
    entity.add_script(DoubleClickHandler(forge, handler, forge.buttons["LEFT"]))

    forge.run()