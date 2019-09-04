import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import os


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.frame = master
        self.createBottomCommandline()


    def createBottomCommandline(self):
        self.frame.columnconfigure(1, weight=1)

        self.history = ScrolledText(root, undo=True)
        self.history.grid(row=3, sticky=W+E+N+S, columnspan=4)


        self.commandLine = Entry(root)
        self.commandLine.grid(row=4, column=0, sticky=W+E+S, columnspan=4)

    def func(event, secondargument, app=""):
        print("You hit return.")
        self.history.insert(END, "hello")


root = tkinter.Tk()
root.geometry("1200x600")
# print(os.getcwd())
app = Application(master=root)
root.bind('<Return>', app.func(app))
app.mainloop()
