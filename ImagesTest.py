from PIL import Image, ImageTk

from tkinter import Tk, Frame, Canvas

class AnImage:

    def __init__(self):
        self.img = Image.new('RGB', (800,600), (0,0,0))
        self.pixels = self.img.load()
        self.x = 10
        self.y = 10
        
        self.pixels[self.x,self.y] = (0,0,255)

    def update(self):
        self.x+=1
        self.y+=2
        self.pixels[self.x,self.y] = (0,0,255)

class TKWindow:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.cnvs = Canvas(frame, width=800, height=600)
        self.cnvs.pack()

    def display_img(self, img):

        self.imgtk = ImageTk.PhotoImage(img)
        self.cnvs.create_image(0,0, image=self.imgtk, anchor='nw')
        
def do_tk_stuff():
    root = Tk()

    an_img = AnImage()

    win = TKWindow(root)

    while 1:
        an_img.update()
        win.display_img(an_img.img)
        root.update()

    # root.mainloop()

if __name__ == "__main__":
    do_tk_stuff()
