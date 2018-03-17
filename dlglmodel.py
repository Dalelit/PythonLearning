import pyglet

class Dl2DModel:
    def draw(self):
        self.vtx_list.draw(pyglet.gl.GL_TRIANGLE_STRIP)

    def move(self, x, y):
        for i in range(0, len(self.vtx_list.vertices), 2):
            self.vtx_list.vertices[i] += x
            self.vtx_list.vertices[i+1] += y
        return self

    def scale(self, x, y):
        for i in range(0, len(self.vtx_list.vertices), 2):
            self.vtx_list.vertices[i] *= x
            self.vtx_list.vertices[i+1] *= y
        return self

    def __str__(self):
        s = str(self.__class__) + " verticies"
        for v in self.vtx_list.vertices:
            s += " {}".format(v)
        return s

class Dl2DTriangle(Dl2DModel):

    def __init__(self):
        vtx_positions = ('v2i', (-1, 0, 1, 0, 0, 1))
        vtx_colours = ('c3B', (255, 0, 0, 0, 255, 0, 0, 0, 255))
        self.vtx_list = pyglet.graphics.vertex_list(3, vtx_positions, vtx_colours)
    
class Dl2DQuad(Dl2DModel):

    def __init__(self):
        vtx_positions = ('v2i', (-1, -1, 1, -1, -1, 1, 1, 1))
        vtx_colours = ('c3B', (255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255))
        self.vtx_list = pyglet.graphics.vertex_list(4, vtx_positions, vtx_colours)
    

def test():
    ttt = Dl2DTriangle()
    print(ttt)
    ttt.scale(100,100)
    ttt.move(100,100)
    print(ttt)
    ttt = Dl2DQuad()
    print(ttt)
    ttt.scale(50,100)
    ttt.move(300,300)
    print(ttt)

if __name__ == '__main__':
    test()
