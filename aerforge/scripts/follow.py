from aerforge import *

class Follow:
    def __init__(self, entity):
        self.entity = entity

    def update(self, entity):
        entity.x = self.entity.x
        entity.y = self.entity.y