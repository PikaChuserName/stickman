import pyglet
from pyglet.window import key

window = pyglet.window.Window()

pyglet.gl.glClearColor(255, 255, 255, 255)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

image = pyglet.image.load('walking.png')
stickman = pyglet.sprite.Sprite(image)
stickman.scale = 0.05

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        stickman.x = stickman.x + 50
    elif symbol == key.LEFT:
        stickman.x = stickman.x - 50
    
                         
@window.event
def on_draw():
    window.clear()
    stickman.draw()

pyglet.app.run()
