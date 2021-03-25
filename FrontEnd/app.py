from tkinter import *
#from PIL import Image, ImageTk



window=Tk()
window.configure(background="red")

#image1 = Image.open("</cs348Image.png>")
#test = ImageTk.PhotoImage(image1)
#label1.place(x=10, y=10)




lbl=Label(window, text="Create Account", fg='white', bg='red', font=("Helvetica", 40))
lbl.place(x=170, y=50)


firstNameLabel=Label(window, text="First Name", fg='black', bg='red', font=("Helvetica", 15))
firstNameLabel.place(x=150, y=150)
firstName=Entry(window, fg='black', bg='red', bd=2)
firstName.place(x=300, y=150)

lastNameLabel=Label(window, text="Last Name", fg='black', bg='red', font=("Helvetica", 15))
lastNameLabel.place(x=150, y=200)
lastName=Entry(window, fg='black', bg='red', bd=2)
lastName.place(x=300, y=200)

emailLabel=Label(window, text="Email", fg='black', bg='red', font=("Helvetica", 15))
emailLabel.place(x=150, y=250)
email=Entry(window, fg='black', bg='red', bd=2)
email.place(x=300, y=250)

userNameLabel=Label(window, text="Username", fg='black', bg='red', font=("Helvetica", 15))
userNameLabel.place(x=150, y=300)
userName=Entry(window, fg='black', bg='red', bd=2)
userName.place(x=300, y=300)

passwordLabel=Label(window, text="Password", fg='black', bg='red', font=("Helvetica", 15))
passwordLabel.place(x=150, y=350)
password=Entry(window, fg='black', bg='red', bd=2, show="*")
password.place(x=300, y=350)

confirmLabel=Label(window, text="Confirm Password", fg='black', bg='red', font=("Helvetica", 15))
confirmLabel.place(x=150, y=400)
confirm=Entry(window, fg='black', bg='red', bd=2, show="*")
confirm.place(x=300, y=400)








def create():
    first = firstName.get()
    last = lastName.get()
    emailText = email.get()
    user = userName.get()
    passwordText = password.get()
    confirmPassword = confirm.get()
    
    print(first + " " + last + " " + emailText + " " + user + " " + passwordText + " " + confirmPassword)
    
    

btn=Button(window, text="Create account", fg='blue', bg='red', command=create)
btn.place(x=220, y=500)
    
    
    





window.title('WhatToWatch')
window.geometry("600x600+10+10")
window.mainloop()


