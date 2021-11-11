from aerforge import *

class Gravity:
    def __init__(self, objects = [], gravity = 0.7, air_friction = 1, ground_friction = 20):
        self.objects = objects

        self.state = False
        self.grounded = False
        self.velocity_x = 0
        self.velocity_y = 0

        self.friction = 0
        self.air_friction = air_friction
        self.ground_friction = ground_friction

        self.gravity = gravity

    def update(self, object):
        object.x = object.x + self.velocity_x
        object.y = object.y + self.velocity_y

        self.state = False

        for i in self.objects:
            if not i.destroyed:
                if object.hit(i):
                    object.y = i.y - object.height + 1
                    self.velocity_y = 0
                    self.grounded = True
                    self.state = True

        if not self.state:
            self.grounded = False

        self.state = False

        if self.grounded:
            self.friction = self.air_friction + self.ground_friction

        else:
            self.friction = self.air_friction

        if self.velocity_x != 0:
            self.velocity_x = self.velocity_x / self.friction

        if not self.grounded:
            self.velocity_y = self.velocity_y + self.gravity