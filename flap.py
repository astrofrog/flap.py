from copy import copy

import pyglet
from pyglet import gl

import settings
from sprites import Bird, Background, Floor, Pipe
from utils import get_sprite, check_collision



def main(callback=None):

    # Initialize window

    window = pyglet.window.Window(width=settings.window_width * settings.scale,
                                  height=settings.window_height * settings.scale,
                                  resizable=False)
    window.clear()

    # To pass to the callback
    def click():
        window.dispatch_event('on_mouse_press')

    # Set up sprites

    bird = Bird(window=window)

    background = Background()

    floor = Floor()

    pipes = []

    tap_to_start = get_sprite('tap.png')

    gameover = get_sprite('gameover.png')

    # Set up game state, which indicates whether the game has started and how long
    # we have to wait until the next pipe appears.


    class GameState(object):

        def __init__(self):
            self.reset()

        def reset(self):
            self.started = False
            self.t_to_next_pipe = 2

    state = GameState()


    def update(dt):

        if not state.started:
            return

        if bird.alive:

            state.t_to_next_pipe -= dt

            if state.t_to_next_pipe < 0:
                pipe = Pipe(space=150, window=window)
                pipes.append(pipe)
                state.t_to_next_pipe += 2

            for pipe in copy(pipes):
                if not pipe.visible:
                    pipes.remove(pipe)

            # Move everything
            background.update(dt)
            for pipe in pipes:
                pipe.update(dt)
            floor.update(dt)

            # Check for collisions
            collision = check_collision(bird, floor) or any([check_collision(bird, pipe) for pipe in pipes])
            if collision or bird.y > window.height:
                bird.die()

        if not bird.dead:
            bird.update(dt)

        if bird.dying and bird.y < -100:
            bird.stop()


    @window.event
    def on_mouse_press(*args):
        if bird.alive:
            bird.flap()
        elif not state.started:
            state.started = True
            bird.start()
            bird.flap()
        elif bird.dead:
            bird.reset()
            pipes.clear()
            state.reset()


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

        if bird.dying or bird.dead:
            gameover.blit(0.5 * (window.width - gameover.width), 0.5 * window.height)

        if callback is not None:

            import numpy as np

            buf = (gl.GLubyte * (3 * window.width * window.height))(0)
            gl.glReadPixels(0, 0, window.width, window.height,
                            gl.GL_RGB,
                            gl.GL_UNSIGNED_BYTE, buf)
            array = np.frombuffer(buf, dtype='<u1')
            array = array.reshape(window.height, window.width, 3)
            array = array[::settings.scale, ::settings.scale]

            callback(array, click, alive=bird.alive)


    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

    pyglet.clock.schedule_interval(update, 0.01)

    pyglet.app.run()


if __name__ == "__main__":

    main()
