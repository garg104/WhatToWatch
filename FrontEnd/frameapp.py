import backend as back
from tkinter import *
from tkinter import ttk
import tkinter as tk
#from PIL import Image, ImageTk

darkred = "#B22222"
textcolor = "white"

class WhatToWatch(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, width=650, height=670, background=darkred)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, HomePage, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    

class StartPage(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700, height=700, background=darkred)
        lbl = tk.Label(self, text="Create Account", fg=textcolor, bg=darkred, font=("Helvetica", 40))
        lbl.place(x=170, y=50)

        self.firstNameLabel = tk.Label(self, text="First Name", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.firstNameLabel.place(x=150, y=150)
        self.firstName = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.firstName.place(x=300, y=150)

        self.lastNameLabel = tk.Label(self, text="Last Name", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.lastNameLabel.place(x=150, y=200)
        self.lastName = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.lastName.place(x=300, y=200)

        self.emailLabel = tk.Label(self, text="Email", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.emailLabel.place(x=150, y=250)
        self.email = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.email.place(x=300, y=250)

        self.userNameLabel = tk.Label(self, text="Username", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.userNameLabel.place(x=150, y=300)
        self.userName = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.userName.place(x=300, y=300)

        self.passwordLabel = tk.Label(self, text="Password", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.passwordLabel.place(x=150, y=350)
        self.password = tk.Entry(self, fg=textcolor, bg=darkred, bd=2, show="*")
        self.password.place(x=300, y=350)

        self.confirmLabel = tk.Label(self, text="Confirm Password", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.confirmLabel.place(x=150, y=400)
        self.confirm = tk.Entry(self, fg=textcolor, bg=darkred, bd=2, show="*")
        self.confirm.place(x=300, y=400)

        self.createBtn = tk.Button(self, text="Create account", command=self.create)
        self.createBtn.place(x=220, y=500)

        #self.retrieveBtn = tk.Button(self, text="Retrieve account", command=self.populateFields)
        #self.retrieveBtn.place(x=220, y=550)
        
        self.LoginBtn = tk.Button(self, text="Login", command=lambda: controller.show_frame("HomePage"))
        self.LoginBtn.place(x=220, y=550)

        print("USER INFO:")
        print(back.getUserInfo())
    
    def clear_fields(self):
        self.firstName.delete(0, 'end')
        self.lastName.delete(0, 'end')
        self.email.delete(0, 'end')
        self.userName.delete(0, 'end')
        self.password.delete(0, 'end')
        self.confirm.delete(0, 'end')
        
    def create(self):
        first = self.firstName.get()
        last = self.lastName.get()
        emailText = self.email.get()
        user = self.userName.get()
        passwordText = self.password.get()
        confirmPassword = self.confirm.get()

        if not first or not last or not emailText or not user or not passwordText or not confirmPassword:
            print("Some field(s) are empty!")
        elif passwordText != confirmPassword:
            print("Passwords are not the same!")
        else:
            print("Inserting with values: " + first + " " + last + " " + emailText + " " +
                  user + " " + passwordText + " " + confirmPassword)
            back.insert(None, self.userName.get(), self.firstName.get(),
                        self.lastName.get(), self.email.get(), self.password.get())
            self.clear_fields()

    def populateFields(self):
        infoLabel = Label(self, text=back.retrieve(self.userName.get()),
                      fg=textcolor, bg=darkred, font=("Helvetica", 15))
        infoLabel.place(x=5, y=590)
    

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=("Helvetica", 40))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=("Helvetica", 40))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()


#window.title('WhatToWatch')
#window.geometry("650x650+10+10")
app = WhatToWatch()
app.mainloop()

back.close()
