import tkinter as tk
from tkinter import *
import random
import time
import sys
import glob
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from database import *
from hands_off import hands_off
from PIL import ImageTk, Image

THEME = 'morph'

class GUI(object):
    
    def __init__(self):

        #Create window
        self.window = tk.Tk()
        self.frame = tk.Frame()
        self.window.title("Hands Off")
        self.popup = ""
        self.state = "Init"
        self.window.style = ttk.Style()
        self.window.style.theme_use(THEME)       
        self._create_welcome_screen()
        self.index = 3
        self.photo = ""
        self.update()

        self.user = None

        self.session = ""

    #Quit
    def quit_win(self):
        # console message
        print("Quitting")

        # Quit
        self.window.quit()

        self.update()

        exit(0)

    #Mainloop GUI
    def loop(self):
        self.window.mainloop()

    #Update GUI
    def update(self):
        self.window.update()

    def _create_welcome_screen(self):
        self.frame.destroy()

        self.window.resizable(1,1)
        self.window.minsize(600,450)
        self.frame = tk.Frame()
        title = tk.Label(self.frame, width=50,pady=30, font=18, text="Welcome to Hands Off!")
        register = tk.Button(self.frame, text="Create a New Account", width=50, pady=30, command=lambda: self._create_register_screen())
        login = tk.Button(self.frame, text='Login to existing account', width=50, pady=30, command=lambda: self._create_login_screen())
        start = tk.Button(self.frame, text='Start', width=50, pady=30, command=lambda: self._on_start_session())
        close = tk.Button(self.frame, text='Close', width=50, pady=30, command=lambda: self.quit_win())
        title.grid(row=0)
        register.grid(row=1)
        login.grid(row=2)
        start.grid(row=4)
        close.grid(row=6)
        self.frame.pack()

        self.state = 'Welcome'

    def _create_login_screen(self):
        # Delete previous frame
        self.frame.destroy()

        self.window.resizable(1, 1) 
        self.window.minsize(500, 300)

        # Create a frame and pack with interface
        self.frame = tk.Frame(self.window)
        title = tk.Label(self.frame, width=50, text='Login', pady=25)
        username = tk.Label(self.frame, text='Username',pady=10)
        password = tk.Label(self.frame, text='Password',pady=10)
        usernameEntry = tk.Entry(self.frame)
        passwordEntry = tk.Entry(self.frame, show='•')
        # redirect to verification
        loginButton = tk.Button(self.frame, text='Login', pady=10, width=15, command=lambda: self._on_submit_login(usernameEntry.get(),passwordEntry.get()))
        backButton = tk.Button(self.frame, text='Back', pady=10, width=15, command=lambda: self._create_welcome_screen())
        title.grid(row=0, columnspan=2)
        username.grid(row=1, column=0)
        usernameEntry.grid(row=1, column=1)
        password.grid(row=2, column=0)
        passwordEntry.grid(row=2, column=1)
        backButton.grid(row=3, column=0)
        loginButton.grid(row=3, column=1)
        self.frame.pack()

        self.state = 'Login'

    def _create_register_screen(self):
        # Delete previous frames
        self.frame.destroy()
        
        self.window.resizable(1, 1) 
        self.window.minsize(500, 300)

        # Create a frame and pack with interface
        self.frame = tk.Frame(self.window)
        title = tk.Label(self.frame, width=50, text='Create a New User', pady=25)
        username = tk.Label(self.frame, text='Username', pady=10)
        password = tk.Label(self.frame, text='Password', pady=10)
        usernameEntry = tk.Entry(self.frame)
        passwordEntry = tk.Entry(self.frame, show='•')
        # redirect to verification
        submitButton = tk.Button(self.frame, text='Submit', pady=5, width=15, command=lambda:self._on_submit_register(usernameEntry.get(),passwordEntry.get()))
        backButton = tk.Button(self.frame, text='Back', pady=5, width=15, command=lambda: self._create_welcome_screen())
        title.grid(row=0, columnspan=2)
        username.grid(row=1, column=0)
        usernameEntry.grid(row=1, column=1)
        password.grid(row=2, column=0)
        passwordEntry.grid(row=2, column=1)
        submitButton.grid(row=3, column=1)
        backButton.grid(row=3, column=0)
        self.frame.pack()

        self.state = 'Register'

    def _on_submit_login(self, username: str, password: str):
        self.user = get_user(username)
        if self.user is None:
            tk.Label(self.frame, width=50, text="User not found.", fg='red', pady=60).grid(row=4,columnspan=2)
        elif self.user[1] == password:
            self._create_welcome_screen()
        else:
            tk.Label(self.frame, width=50, text="Incorrect password.", fg='red', pady=60).grid(row=4,columnspan=2)
    
    def _on_submit_register(self, username: str, password: str):
        user_created = False
        if(len(username)==0 or len(password)==0):
            tk.Label(self.frame, width=50, text="Username and password cannot be empty.", fg='red', pady=60).grid(row=4,columnspan=2)
        else:
            user_created = create_user(username, password)

        if user_created:
            self.user = get_user(username)
            self._create_welcome_screen()
        else:
            tk.Label(self.frame, width=50, text="User with that username already exists.", fg='red', pady=60).grid(row=4,columnspan=2)
    
    def _on_start_session(self):
        if(self.user):
            self._create_session()
        else:
            tk.Label(self.frame, width=50, text="You are not logged in", fg='red', pady=60).grid(row=8,columnspan=2)
    
    def _create_session(self):

        #Starts session
        currentRate = hands_off()
        self._results(currentRate)

    def _results(self, currentRate):
        global image_frame, i_open, i_size
        self.frame.destroy()
        print(self.user)
        self.index = (self.index + 1) % 3
        i_open = (Image.open("code/eye_rubs/frame" + str(self.index) + ".png"))
        i_size = i_open.resize((320,240), Image.ANTIALIAS)
        i_size.save("test.png")
        self.frame.destroy()
        self.window.resizable(1,1)
        self.window.minsize(640,480)
        self.frame = tk.Frame()
        canvas = tk.Canvas(self.frame, width = 300, height = 200, bg='white', highlightthickness=0)
        canvas.grid(row=5, pady=10)
        image_frame = ImageTk.PhotoImage(i_size)
        canvas.create_image(0,0, anchor="nw", image=image_frame)
        currentAverage = get_average(currentRate)
        title = tk.Label(self.frame, pady=20, width=50, font=18, text="Session Complete!")
        register = tk.Label(self.frame, pady=30, width=50, text="You touched your eyes at a rate of "+str(round(currentRate,2))+" Times per minute!")
        average = tk.Label(self.frame, pady=30, width=50, text='The global average is '+ str(round(currentAverage,2)) +' Times per minute')
        next = tk.Button(self.frame, pady=30, text='Next', width=50, command=lambda: self._results(currentRate))
        done = tk.Button(self.frame, pady=30, text='Done', width=50, command=lambda: self._create_welcome_screen())
        title.grid(row=0)
        register.grid(row=1)     
        average.grid(row=2)
        next.grid(row=3, pady=10)
        done.grid(row=4)  
        self.frame.pack()
