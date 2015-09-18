import random
from utils import get_sprite
from bbox import BBox

class PipeSet(object):

    def __init__(self, scale, space, window):

        # Load bird in different states

        self.sprite_bot = get_sprite('sprites/pipe_bot.png', scale=scale)
        self.sprite_top = get_sprite('sprites/pipe_top.png', scale=scale)
        self.dx = self.sprite_bot.width
        self.dy = self.sprite_bot.height
        self.space = space
        self.x = window.width
        self.vx = -100
        self.wx = window.width
        self.wy = window.height
        self.y0 = -self.dy / 2 + random.uniform(0, self.dy / 2.)

    def update(self, dt):
        self.x += self.vx * dt

    @property
    def visible(self):
        return self.x >= -self.dx and self.x <= self.wx

    def blit(self):
        self.sprite_bot.blit(self.x, self.y0)
        self.sprite_top.blit(self.x, self.y0 + self.dy + self.space)

    @property
    def bboxes(self):
        return [BBox(self.x, self.y0, self.dx, self.dy),
                BBox(self.x, self.y0 + self.dy + self.space, self.dx, self.dy)]

    def stop(self):
        self.vx = 0