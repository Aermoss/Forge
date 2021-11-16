from aerforge import *

class Follow:
    def __init__(self, entity):
        self.entity = entity

    def update(self, entity):
        entity.x, entity.y = self.entity.x, self.entity.y