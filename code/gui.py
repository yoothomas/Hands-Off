import tkinter as tk

class GUI(object):
    
    def __init__(self):

        #Create window
        self.window = tk.Tk()
        self.window.title("###PROJECTNAME")
        
        self. _base_window()
        self._welcome_screen()
    
        self.update()

        self.session = ""

    def _base_window(self):

        self.window.resizable(1,1)
        self.window.minsize(600,450)
        self.frame = tk.Frame()
        self.popup = ""
        self.state = "Init"

    def _welcome_screen(self):

        self.frame.destroy()

        self._base_window()

        title = tk.Label(self.frame, width=50, text="Welcome to Project!")
        register 

        

    #Mainloop GUI
    def loop(self):
        self.window.mainloop()

    #Update GUI
    def update(self):
        self.window.update()