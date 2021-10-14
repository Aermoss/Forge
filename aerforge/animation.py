import os

class Animation:
    def __init__(self, time, folder = "."):
        self.frames = []
        self.time = time
        self.folder = folder
        
        if folder != ".":
            for file in os.listdir(folder):
                self.frames.append(file)

        self.frames = sorted(self.frames)
        self.pos = len(self.frames)

    def sort(self):
        self.frames = sorted(self.frames)