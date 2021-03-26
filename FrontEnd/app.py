import backend as back
from tkinter import *
from tkinter import ttk
#from PIL import Image, ImageTk

darkred = "#B22222"
textcolor = "white"

window = Tk()
window.configure(background=darkred)

#image1 = Image.open("</cs348Image.png>")
#test = ImageTk.PhotoImage(image1)
#label1.place(x=10, y=10)


lbl = Label(window, text="Create Account", fg=textcolor,
            bg=darkred, font=("Helvetica", 40))
lbl.place(x=170, y=50)


firstNameLabel = Label(window, text="First Name",
                       fg=textcolor, bg=darkred, font=("Helvetica", 15))
firstNameLabel.place(x=150, y=150)
firstName = Entry(window, fg=textcolor, bg=darkred, bd=2)
firstName.place(x=300, y=150)

lastNameLabel = Label(window, text="Last Name", fg=textcolor,
                      bg=darkred, font=("Helvetica", 15))
lastNameLabel.place(x=150, y=200)
lastName = Entry(window, fg=textcolor, bg=darkred, bd=2)
lastName.place(x=300, y=200)

emailLabel = Label(window, text="Email", fg=textcolor,
                   bg=darkred, font=("Helvetica", 15))
emailLabel.place(x=150, y=250)
email = Entry(window, fg=textcolor, bg=darkred, bd=2)
email.place(x=300, y=250)

userNameLabel = Label(window, text="Username", fg=textcolor,
                      bg=darkred, font=("Helvetica", 15))
userNameLabel.place(x=150, y=300)
userName = Entry(window, fg=textcolor, bg=darkred, bd=2)
userName.place(x=300, y=300)

passwordLabel = Label(window, text="Password", fg=textcolor,
                      bg=darkred, font=("Helvetica", 15))
passwordLabel.place(x=150, y=350)
password = Entry(window, fg=textcolor, bg=darkred, bd=2, show="*")
password.place(x=300, y=350)

confirmLabel = Label(window, text="Confirm Password",
                     fg=textcolor, bg=darkred, font=("Helvetica", 15))
confirmLabel.place(x=150, y=400)
confirm = Entry(window, fg=textcolor, bg=darkred, bd=2, show="*")
confirm.place(x=300, y=400)

print("USER INFO:")
print(back.getUserInfo())


def create():
    first = firstName.get()
    last = lastName.get()
    emailText = email.get()
    user = userName.get()
    passwordText = password.get()
    confirmPassword = confirm.get()

    if not first or not last or not emailText or not user or not passwordText or not confirmPassword:
        print("Some field(s) are empty!")
    elif passwordText != confirmPassword:
        print("Passwords are not the same!")
    else:
        print("Inserting with values: " + first + " " + last + " " + emailText + " " +
              user + " " + passwordText + " " + confirmPassword)
        back.insert(None, userName.get(), firstName.get(),
                    lastName.get(), email.get(), password.get())
        clear_fields()


def clear_fields():
    firstName.delete(0, 'end')
    lastName.delete(0, 'end')
    email.delete(0, 'end')
    userName.delete(0, 'end')
    password.delete(0, 'end')
    confirm.delete(0, 'end')


def populateFields():
    infoLabel = Label(window, text=back.retrieve(userName.get()),
                      fg=textcolor, bg=darkred, font=("Helvetica", 15))
    infoLabel.place(x=5, y=590)


createBtn = ttk.Button(window, text="Create account", command=create)
createBtn.place(x=220, y=500)

retrieveBtn = ttk.Button(
    window, text="Retrieve account", command=populateFields)
retrieveBtn.place(x=220, y=550)


window.title('WhatToWatch')
window.geometry("650x650+10+10")
window.mainloop()

back.close()
