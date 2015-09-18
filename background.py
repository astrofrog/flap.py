from utils import get_sprite
from bbox import BBox

class Background(object):
    
    def __init__(self, scale):

        # Load bird in different states

        self.sprite = get_sprite('sprites/background.png', scale=scale)
        self.dx = self.sprite.width
        self.dy = self.sprite.height
        self.x = 0
        self.vx = -50

    def update(self, dt):

        # Update background position
        self.x += self.vx * dt
        if self.x < -self.dx:
            self.x += self.dx

    def blit(self):
        self.sprite.blit(self.x, 0)
        self.sprite.blit(self.x + self.dx, 0)
        
    @property
    def bboxes(self):
        return []

    def stop(self):
        self.vx = 0

class Floor(object):
    
    def __init__(self, scale):

        # Load bird in different states

        self.sprite = get_sprite('sprites/floor.png', scale=scale)
        self.dx = self.sprite.width
        self.dy = self.sprite.height
        self.x = 0
        self.vx = -100

    def update(self, dt):

        # Update background position
        self.x += self.vx * dt
        if self.x < -self.dx:
            self.x += self.dx

    def blit(self):
        self.sprite.blit(self.x, -50)
        self.sprite.blit(self.x + self.dx, -50)
        
    @property
    def bboxes(self):
        return [BBox(self.x, -50, self.dx * 2, self.dy)]

    def stop(self):
        self.vx = 0