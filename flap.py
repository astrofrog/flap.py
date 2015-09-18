from copy import copy

import pyglet
from pyglet.gl import GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, glEnable, glBlendFunc

import settings
from sprites import Bird, Background, Floor, PipeSet
from utils import get_sprite, check_collision

# Initialize window

window = pyglet.window.Window(width=settings.window_width * settings.scale,
                              height=settings.window_height * settings.scale, resizable=False)
window.clear()

#These arguments are x, y and z respectively. This scales your window.
# glScalef(4.0, 4.0, 4.0)

bird = Bird(scale=settings.scale,
            x_start=window.width * 0.5,
            y_start=window.height * 0.55)

background = Background(scale=settings.scale)
floor = Floor(scale=settings.scale)

pipes = []


class GameState(object):

    def __init__(self):
        self.started = False
        self.t_to_next_pipe = 2


tap_to_start = get_sprite('sprites/tap.png', scale=settings.scale)
gameover = get_sprite('sprites/gameover.png', scale=settings.scale)

state = GameState()


def update(dt):

    if not state.started:
        return

    if bird.alive:

        state.t_to_next_pipe -= dt

        if state.t_to_next_pipe < 0:
            pipe = PipeSet(scale=settings.scale, space=150, window=window)
            pipes.append(pipe)
            state.t_to_next_pipe += 2

        for pipe in copy(pipes):
            if not pipe.visible:
                pipes.remove(pipe)

        bird.update(dt)
        background.update(dt)
        for pipe in pipes:
            pipe.update(dt)
        floor.update(dt)

        # Check for collisions
        collision = check_collision(bird, floor) or any([check_collision(bird, pipe) for pipe in pipes])
        if collision:
            bird.die()

    if not bird.dead:
        bird.update(dt)

    if bird.dying and check_collision(bird, floor):
        bird.stop()


@window.event
def on_mouse_press(*args):
    if bird.alive:
        bird.flap()
    elif not state.started:
        state.started = True
        bird.start()
        bird.flap()


@window.event
def on_draw():

    window.clear()
    background.blit()
    for pipe in pipes:
        pipe.blit()
    floor.blit()
    bird.blit()

    if not state.started:
        tap_to_start.blit(0.5 * (window.width - tap_to_start.width * 0.37), 0.43 * window.height)
    
    if state.started and bird.dead:
        gameover.blit(0.5 * (window.width - gameover.width), 0.5 * window.height)


glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

pyglet.clock.schedule_interval(update, 0.01)

pyglet.app.run()
