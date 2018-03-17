import pyglet
from dlglmodel import *

class DlGlWindow(pyglet.window.Window):

    def __init__(self):
        super().__init__(800,600)
        # self.set_fullscreen(True)
        self.keyboard = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keyboard)

        self.models = []
        self.models.append(Dl2DTriangle())
        self.models.append(Dl2DQuad().scale(50,50).move(100,100))
        self.models.append(Dl2DTriangle().scale(100,200).move(200,300))

        # pyglet.clock.schedule_interval(self.some_func, time in seconds)
        # def some_func(self, dt):

    def on_draw(self):
        self.clear()
        for m in self.models:
            m.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.mousepos = (x, y)


def main():
    win = DlGlWindow()
    pyglet.app.run()

if __name__ == '__main__':
    main()
