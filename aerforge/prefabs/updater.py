import threading

class Updater:
    def __init__(self):
        self.handlers = []

        thread = threading.Thread(target = self._update)
        thread.start()

    def _update(self):
        while True:
            for i in self.handlers:
                i()

    def update(self, fn):
        self.handlers.append(fn)