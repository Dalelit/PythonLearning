import pyglet
from pyglet.window import Window
from pyglet.window import key
from pyglet.window.key import KeyStateHandler
from pyglet.text import Label
from pyglet import image

win = Window()
keyboard = KeyStateHandler()
win.push_handlers(keyboard)

winWidth, winHeight = win.get_size()
mouseX = 0
mouseY = 0

label = Label('Hello')

cnvs = win.canvas
print(dir(cnvs))
print(cnvs.__class__)
disp = win.canvas.display
print(dir(disp))
print(disp.__class__)


# screens = display.get_screens()
# print(win.context)
# print("screen count {}".format(len(screens)))
# print(screens[0])
# print(display)

vtx_positions = ('v2i', (0, 0, winWidth, winHeight))
vtx_colours = ('c3B', (0, 255, 255, 255, 255, 0))
print(vtx_positions)
print(vtx_colours)

vlist1 = pyglet.graphics.vertex_list(2, vtx_positions, vtx_colours)

def image_test():
    print("Image test")


def do_stuff():
    # label.text = "do stuff"
    # if keyboard[key.UP] or keyboard[key.DOWN]:
    #     label.text += "-moving direct"
    # if keyboard[key.LEFT] or keyboard[key.RIGHT]:
    #     label.text += "-moving sideways"
    if keyboard[key.SPACE]:
        image_test()

    

@win.event
def on_draw():
    win.clear()
    do_stuff()
    vlist1.draw(pyglet.gl.GL_LINES)
    # label.draw()

@win.event
def on_mouse_motion(x, y, dx, dy):
    mouseX = x
    mouseY = y
    vlist1.vertices[:2] = [x, y]

#@window.event
# def on_key_press(symbol, modifiers):
#     if symbol >= key.A and symbol <= key.Z:
#         label.text = "Pressed a letter"
#     else:
#         label.text = "something else"
#

pyglet.app.run()
