import pyglet
from pyglet.window import key

window = pyglet.window.Window()

pyglet.gl.glClearColor(255, 255, 255, 255)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

image = pyglet.image.load('walking.png')
image2 = pyglet.image.load('platform.jpg')
stickman = pyglet.sprite.Sprite(image)
platform = pyglet.sprite.Sprite(image2)
stickman.scale = 0.05
platform.scale = 0.2
platform.x = 350

stickman.move_right = False
stickman.move_left = False

def main():
    pyglet.clock.schedule_interval(update, 1/60.0) #update at 60Hz   
    pyglet.app.run()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        stickman.move_right = True
    elif symbol == key.LEFT:
        stickman.move_left = True

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.RIGHT:
        stickman.move_right = False
    elif symbol == key.LEFT:
        stickman.move_left = False
   
def collide(stickman, platform, x=0, y=0):
    if y + stickman.y + stickman.height < platform.y:
        return False
    if y + stickman.y > platform.y + platform.height:
        return False
    if x + stickman.x + stickman.width < platform.x:
        return False
    if x + stickman.x > platform.x + platform.width:
        return False
    return True 
        
def update(dt):
    x = 75 * dt
    if stickman.move_right:
        if not collide(stickman, platform, x, 0):
            stickman.x += x
    elif stickman.move_left:
        if not collide(stickman, platform, -x, 0):
            stickman.x -= x
      

@window.event
def on_draw():
    window.clear()
    stickman.draw()
    platform.draw()

if __name__ == "__main__":
    main()
