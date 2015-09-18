import pyglet
from pyglet.gl import *

def get_sprite(filename, scale):
    image = pyglet.image.load(filename)
    texture = image.get_texture()
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
    texture.width = texture.width * scale
    texture.height = texture.height * scale    
    return texture
