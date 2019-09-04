import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from SMLNetworking.net import netHelper

import os

class FirstConnectWindow(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.shallContinue = False
        self.ip = Entry(root)
        self.deviceType = Entry(root)
        self.username = Entry(root)
        self.password = Entry(root)
        self.ipLabel = Label(root, text="IP")
        self.deviceTypeLabel = Label(root, text="Device Type")
        self.usernameLabel = Label(root, text="Username")
        self.passwordLabel = Label(root, text="Password")
        self.connectButton = Button(root, text="Connect")

        self.ipLabel.grid(row=1)
        self.deviceTypeLabel.grid(row=1, column=1)
        self.usernameLabel.grid(row=1, column=2)
        self.passwordLabel.grid(row=1, column=3)

        self.ip.grid(row=2)
        self.deviceType.grid(row=2, column=1)
        self.username.grid(row=2, column=2)
        self.password.grid(row=2, column=3)

        self.connectButton.grid(row=3)
        self.connectButton['command'] = self.connect

    def connect(self):
        print(self.ip.get())
        if(netHelper.connecting(ip=self.ip.get(), device_type=self.deviceType.get(), username=self.username.get(), password=self.password.get())):
            self.shallContinue = True
            self.master.destroy()

        else:
            pass
            # add another label

      #  netHelper.connecting(ip=self.ip.get(), device_type=self.deviceType.get(), username=self.username.get(), password=self.password.get())


root = tkinter.Tk()
root.geometry("600x300")
# print(os.getcwd())
fcw = FirstConnectWindow(master=root)
fcw.mainloop()
#if(fcw.shallContinue == False):
#    sys.exit()




class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.frame = master
        self.createBottomCommandline()
        self.frame.bind('<Return>', self.hittedEnter(self=self))


    def createBottomCommandline(self):
        self.frame.columnconfigure(1, weight=1)

        self.history = ScrolledText(root, undo=True)
        self.history.grid(row=3, sticky=W+E+N+S, columnspan=4)

        self.commandLine = Entry(root)
        self.commandLine.grid(row=4, column=0, sticky=W+E+S, columnspan=4)

    def hittedEnter(event, self):
        result = netHelper.custom_command(self.commandLine.get())
        self.history.insert(END, result)



root = tkinter.Tk()
root.geometry("1200x600")
# print(os.getcwd())
app = Application(master=root)

app.mainloop()
