import tkinter as tk

class GUI(object):
    
    def __init__(self):

        #Create window
        self.window = tk.Tk()
        self.window.title("###PROJECTNAME")
        self.window.resizable(1,1)
        self.window.minsize(600,450)
        self.frame = tk.Frame()
        self.popup = ""
        self.state = "Init"


        self.update()

        self.session = ""

    #Mainloop GUI
    def loop(self):
        self.window.mainloop()

    #Update GUI
    def update(self):
        self.window.update()