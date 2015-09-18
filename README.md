About
=====

This is a simplistic clone of flappy bird, still very much in development. The
aim is to be able to use it to test out machine learning algorithms.

![screenshot](flappy_screenshot.png)

Install
=======

The only dependency is [pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home).
You can install it with::

    pip install pyglet

Once this is installed, simply run::

    python flap.py

in this repository.

Machine learning
================

If you want to try and make an algorithm that will successfully play the game,
write a separate script then do:

    from flap import main

to import the main function to run the game. You should then define a callback
function that looks like:

    def callback(array, click, alive):
        pass

This callback function will get called every time the window is drawn. The
arguments passed are:

* ``array``: an (ny, nx, 3) RGB array of the screen
* ``click``: a function you can call to click
* ``alive``: a boolean telling you whether the bird is alive

you can then start the game with:

    main(callback=callback)

Note that you will need to click once to start the game. If the game stops, you
can click twice to start again.

Missing features
================

* Keeping track of score
* Tilting bird when flying up and down

Credits
=======

[Original game](https://en.wikipedia.org/wiki/Flappy_Bird) by Dong Nguyen.

Spires downloaded from [here](http://www.spriters-resource.com/mobile/flappybird/sheet/59537/)