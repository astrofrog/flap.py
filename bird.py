from utils import get_sprite

from bbox import BBox

class Bird(object):
    """
    The flappy bird!
    """

    def __init__(self, scale, x_start, y_start):

        # Load bird in different states

        self.sprite_lib = [get_sprite('sprites/bird1.png', scale=scale),
                           get_sprite('sprites/bird2.png', scale=scale),
                           get_sprite('sprites/bird3.png', scale=scale)]
        self.sprite_lib.append(self.sprite_lib[1])

        self.curr_id = 1

        self.flap_dt = 0.1
        self.flap_t = 0

        self.x = x_start
        self.y = y_start
        self.vy = 0
        self.ay = -500

        self.dx = self.sprite.width
        self.dy = self.sprite.height
        
        self.state = 0
        
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
        self.vy = 100
        
    def stop(self):
        self.state = 0
        self.vy = 0
        self.ay = 0

    @property
    def sprite(self):
        return self.sprite_lib[self.curr_id % 4]

    def flap(self):
        self.vy = 250

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
        
