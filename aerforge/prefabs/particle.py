from aerforge import *
from aerforge.prefabs import *

import time
import random

class ParticleGenerator:
    def __init__(self, window):
        self.window = window

        self.particles = []

    def update(self):
        for particle in self.particles:
            if particle.destroyed:
                self.particles.pop(self.particles.index(particle))

            particle.update()
            particle.draw()

    def create(self, shape = Rect, x = 0, y = 0, width = 10, height = 10, color = Color(240, 240, 240), amount = 30, max_force_x = 10, max_force_y = 10, gravity = 0, destroy_particle = True, animate = True, min_destroy_time = 0, max_destroy_time = 2, width_decrease_amount = 1, height_decrease_amount = 1):
        for i in range(amount):
            particle = Particle(window = self.window, shape = shape, width = width, height = height, x = x, y = y, color = color, destroy_particle = destroy_particle, animate = animate, destroy_time = random.uniform(min_destroy_time, max_destroy_time), width_decrease_amount = width_decrease_amount, height_decrease_amount = height_decrease_amount)
            particle.gravity.gravity = gravity
            particle.gravity.force(random.randint(-max_force_x, max_force_x), random.randint(-max_force_y, max_force_y))
            self.particles.append(particle)

    def center(self):
        for particle in self.particles:
            particle.center()

    def destroy(self):
        for particle in self.particles:
            particle.destroy()

        self.particles = []

class Particle(GameObject):
    def __init__(self, window, shape = Rect, x = 0, y = 0, width = 10, height = 10, color = Color(240, 240, 240), destroy_particle = True, animate = True, destroy_time = 2, width_decrease_amount = 10, height_decrease_amount = 10):
        super().__init__(
            window = window,
            shape = shape,
            color = color,
            width = width,
            height = height,
            x = x,
            y = y,
        )

        self.gravity = Gravity(self)

        self.destroy_time = destroy_time
        self.spawn_time = time.time()
        self.width_decrease_amount = width_decrease_amount
        self.height_decrease_amount = height_decrease_amount
        self.destroy_particle = destroy_particle
        self.animate = animate

    def update(self):
        self.gravity.update()

        if self.destroy_particle:
            if self.spawn_time + self.destroy_time < time.time():
                if self.animate:
                    self.width, self.height = self.width - self.width_decrease_amount, self.height - self.height_decrease_amount
                    self.x, self.y = self.x + self.width_decrease_amount / 2, self.y + self.height_decrease_amount / 2

                    if self.width <= 0 and self.height <= 0:
                        self.destroy()

                else:
                    self.destroy()

if __name__ == "__main__":
    forge = Forge()

    particle = ParticleGenerator(forge)

    counter = FpsCounter

    state = False

    while True:
        if forge.input.mouse_pressed():
            if state:
                mouse_x, mouse_y = forge.input.mouse_pos()
                particle.create(x = mouse_x, y = mouse_y)
                state = False

        else:
            state = True

        particle.update()
        forge.update()