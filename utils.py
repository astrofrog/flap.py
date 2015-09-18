import pyglet
from pyglet.gl import gl


def get_sprite(filename, scale):
    image = pyglet.image.load(filename)
    texture = image.get_texture()
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
    texture.width = texture.width * scale
    texture.height = texture.height * scale    
    return texture


class BBox(object):
    def __init__(self, x, y, dx, dy):
        self.xmin = x
        self.xmax = x + dx
        self.ymin = y
        self.ymax = y + dy


def check_collision(a, b):
    for b1 in a.bboxes:
        for b2 in b.bboxes:
            if b1.xmax < b2.xmin or b1.xmin > b2.xmax or b1.ymax < b2.ymin or b1.ymin > b2.ymax:
                continue
            else:
                return True
        