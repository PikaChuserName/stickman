import pyglet
from pyglet.window import key

image = pyglet.image.load('background.gif')
background = pyglet.sprite.Sprite(image)
background.scale = 1.5

window = pyglet.window.Window(width=background.width, height=background.height)

pyglet.gl.glClearColor(255, 255, 255, 255)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

image2 = pyglet.image.load('genji.png')
image3 = pyglet.image.load('platform.jpg')
image4 = pyglet.image.load('platform.jpg')
stickman = pyglet.sprite.Sprite(image2)
platform = pyglet.sprite.Sprite(image3)
platform2 = pyglet.sprite.Sprite(image4)
stickman.scale = 0.2
platform.scale = 0.2
platform.x = 350
platform2.scale = 0.2
platform2.x = 500
platform2.y = 150

platforms = [platform, platform2]

stickman.yspeed = 0
stickman.xspeed = 0

def main():
    pyglet.clock.schedule_interval(update, 1/60.0) #update at 60Hz   
    pyglet.app.run()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        stickman.xspeed = 100
    elif symbol == key.LEFT:
        stickman.xspeed = -100
    elif symbol == key.SPACE:
        stickman.yspeed = 250


@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.RIGHT:
        stickman.xspeed = 0
    elif symbol == key.LEFT:
        stickman.xspeed = 0
   
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
    
def collide_all(stickman, objects, x=0, y=0):
    for obj in objects:
        if collide(stickman, obj, x, y): 
            return True
    
def update(dt):
    x = stickman.xspeed * dt
    y = stickman.yspeed * dt
    if not collide_all(stickman, platforms, x, y):
        stickman.x += x
        stickman.y += y
    
        if stickman.x < 0:
            stickman.x -= x
        if stickman.y > 0:
            stickman.yspeed -= 300 * dt 
        else:
            stickman.y = 0
            stickman.yspeed = 0    
           

@window.event
def on_draw():
    window.clear()
    background.draw()
    stickman.draw()
    platform.draw()
    platform2.draw()

if __name__ == "__main__":
    main()
