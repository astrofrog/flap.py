import random
from utils import get_sprite, BBox


class Pipe(object):

    def __init__(self, scale, space, window):
        self.sprite_bot = get_sprite('pipe_bot.png', scale=scale)
        self.sprite_top = get_sprite('pipe_top.png', scale=scale)
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


class Background(object):

    def __init__(self, scale):
        self.sprite = get_sprite('background.png', scale=scale)
        self.dx = self.sprite.width
        self.dy = self.sprite.height
        self.x = 0
        self.y = 0
        self.vx = -50

    def update(self, dt):
        self.x += self.vx * dt
        if self.x < -self.dx:
            self.x += self.dx

    def blit(self):
        self.sprite.blit(self.x, self.y)
        self.sprite.blit(self.x + self.dx, self.y)

    @property
    def bboxes(self):
        return []

    def stop(self):
        self.vx = 0


class Floor(Background):

    def __init__(self, scale):
        self.sprite = get_sprite('floor.png', scale=scale)
        self.dx = self.sprite.width
        self.dy = self.sprite.height
        self.x = 0
        self.y = -50
        self.vx = -100

    @property
    def bboxes(self):
        return [BBox(self.x, self.y, self.dx * 2, self.dy)]

    def stop(self):
        self.vx = 0


class Bird(object):
    """
    The flappy bird!
    """

    def __init__(self, scale, window):

        # Load bird in different states

        self.sprite_lib = [get_sprite('bird1.png', scale=scale),
                           get_sprite('bird2.png', scale=scale),
                           get_sprite('bird3.png', scale=scale)]
        self.sprite_lib.append(self.sprite_lib[1])

        self.window = window

        self.reset()

        self.dx = self.sprite.width
        self.dy = self.sprite.height

    def reset(self):
        self.x = self.window.width * 0.5
        self.y = self.window.height * 0.55
        self.vy = 0
        self.ay = -2000
        self.state = 3
        self.flap_dt = 0.1
        self.flap_t = 0
        self.curr_id = 1

    @property
    def alive(self):
        return self.state == 2

    @property
    def dying(self):
        return self.state == 1

    @property
    def dead(self):
        return self.state == 0

    def start(self):
        self.state = 2

    def die(self):
        self.state = 1
        self.ay *= 2
        self.vy = 200

    def stop(self):
        self.state = 0
        self.vy = 0
        self.ay = 0

    @property
    def sprite(self):
        return self.sprite_lib[self.curr_id % 4]

    def flap(self):
        self.vy = 400

    def update(self, dt):

        # Flapping

        self.flap_t += dt

        if self.flap_t > self.flap_dt:
            self.curr_id += 1
            self.flap_t = 0

        # Physics

        self.vy += dt * self.ay
        self.y += self.vy * dt

    def blit(self):
        self.sprite.blit(self.x - 0.5 * self.dx,
                         self.y - 0.5 * self.dy)

    @property
    def bboxes(self):
        return [BBox(self.x - 0.5 * self.dx, self.y - 0.5 * self.dy, self.dx, self.dy)]
