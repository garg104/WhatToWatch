import backend as back
from tkinter import *
from tkinter import ttk
import tkinter as tk
#from PIL import Image, ImageTk

darkred = "#B22222"
textcolor = "white"


class WhatToWatch(tk.Tk):

    userID = "19"
    currMovieID = "1817232"
    # currMovieID = "249516"
    #currMovieID = "12876132"
    

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, width=650, height=670, background=darkred)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, HomePage, NewReviewPage, ViewMovieReviewsPage, ViewUserReviewsPage, ViewSearchMovies):
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
        tk.Frame.__init__(self, parent, width=700,
                          height=700, background=darkred)
        lbl = tk.Label(self, text="Create Account", fg=textcolor,
                       bg=darkred, font=("Helvetica", 40))
        lbl.place(x=170, y=50)

        self.firstNameLabel = tk.Label(
            self, text="First Name", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.firstNameLabel.place(x=150, y=150)
        self.firstName = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.firstName.place(x=300, y=150)

        self.lastNameLabel = tk.Label(
            self, text="Last Name", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.lastNameLabel.place(x=150, y=200)
        self.lastName = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.lastName.place(x=300, y=200)

        self.emailLabel = tk.Label(
            self, text="Email", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.emailLabel.place(x=150, y=250)
        self.email = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.email.place(x=300, y=250)

        self.userNameLabel = tk.Label(
            self, text="Username", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.userNameLabel.place(x=150, y=300)
        self.userName = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.userName.place(x=300, y=300)

        self.passwordLabel = tk.Label(
            self, text="Password", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.passwordLabel.place(x=150, y=350)
        self.password = tk.Entry(
            self, fg=textcolor, bg=darkred, bd=2, show="*")
        self.password.place(x=300, y=350)

        self.confirmLabel = tk.Label(
            self, text="Confirm Password", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.confirmLabel.place(x=150, y=400)
        self.confirm = tk.Entry(self, fg=textcolor, bg=darkred, bd=2, show="*")
        self.confirm.place(x=300, y=400)

        # self.createBtn = tk.Button(
        #     self, text="Create account", command=self.create)
        self.createBtn = ttk.Button(
            self, text="Create account", command=self.create)
        self.createBtn.place(x=220, y=500)

        #self.retrieveBtn = tk.Button(self, text="Retrieve account", command=self.populateFields)
        #self.retrieveBtn.place(x=220, y=550)

        self.LoginBtn = ttk.Button(
            self, text="Login", command=lambda: controller.show_frame("HomePage"))
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

    def login(self):
        user = self.userName.get()
        psswrd = self.password.get()
        WhatToWatch.userID = str(back.login(user, psswrd))
        print(WhatToWatch.userID)
        if WhatToWatch.userID is not None:
            WhatToWatch.show_frame("HomePage")



class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700,
                          height=700, background=darkred)
        self.controller = controller
        self.label = tk.Label(self, text="Home", font=("Helvetica", 40))
        self.label.pack(side="top", fill="x", pady=10)

        self.newReviewBtn = ttk.Button(
            self, text="Write New Review", command=lambda: controller.show_frame("NewReviewPage"))
        self.newReviewBtn.place(relx=0.5, y=250, anchor=CENTER)

        self.viewReviewsBtn = ttk.Button(
            self, text="View Movie Reviews", command=lambda: controller.show_frame("ViewMovieReviewsPage"))
        self.viewReviewsBtn.place(relx=0.5, y=300, anchor=CENTER)

        self.viewReviewsBtn = ttk.Button(
            self, text="View User Reviews", command=lambda: controller.show_frame("ViewUserReviewsPage"))
        self.viewReviewsBtn.place(relx=0.5, y=350, anchor=CENTER)

        self.viewSearchBtn = ttk.Button(
            self, text="Search Movies", command=lambda: controller.show_frame("ViewSearchMovies"))
        self.viewSearchBtn.place(relx=0.5, y=400, anchor=CENTER)

        self.logoutBtn = ttk.Button(
            self, text="Logout", command=lambda: controller.show_frame("StartPage"))
        self.logoutBtn.place(relx=0.5, y=450, anchor=CENTER)
        
        self.deleteBtn = ttk.Button(
            self, text="Delete Account", command=lambda: self.deleteAccount(controller))
        self.deleteBtn.place(relx=0.5, y=500, anchor=CENTER)
        
    def deleteAccount(self, controller):
        print("account delete clicked")
        print(WhatToWatch.userID)
        delete = back.deleteUser(WhatToWatch.userID)
        print(delete)
        controller.show_frame("StartPage")


class NewReviewPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700,
                          height=700, background=darkred)
        self.controller = controller
        label = tk.Label(self, text="Movie Review", font=("Helvetica", 40))
        label.pack(side="top", fill="x", pady=10)

        self.movidIDLabel = tk.Label(self, text="Movie ID", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.movidIDLabel.place(x=150, y=150)
        self.movieID = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.movieID.place(x=300, y=150)
        
        self.ratingLabel = tk.Label(
            self, text="Rating (1-10)", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.ratingLabel.place(x=150, y=200)
        self.rating = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.rating.place(x=300, y=200)

        self.commentLabel = tk.Label(
            self, text="Comment", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.commentLabel.place(x=150, y=250)
        self.comment = tk.Text(self, height=5, width=50)
        self.comment.place(x=300, y=250)

        self.submitButton = ttk.Button(
            self, text="Submit Review", command=self.submitReview)
        self.submitButton.place(relx=0.5, y=400, anchor=CENTER)

        self.homeButton = ttk.Button(
            self, text="Cancel", command=lambda: controller.show_frame("HomePage"))
        self.homeButton.place(relx=0.5, y=550, anchor=CENTER)

    def submitReview(self):
        userID = WhatToWatch.userID
        movieID = self.movieID.get()
        rating = self.rating.get()
        comment = self.comment.get("1.0", END)
        back.newReview(userID, movieID, rating, comment)


class ViewMovieReviewsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700,
                          height=700, background=darkred)
        self.controller = controller
        label = tk.Label(self, text="Reviews", font=("Helvetica", 40))
        label.pack(side="top", fill="x", pady=10)

        self.movieLabel = tk.Label(
            self, text="Movie ID: " + WhatToWatch.currMovieID, fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.movieLabel.place(x=65, y=90)

        num_movie_reviews = str(
            back.getNumMovieReviews(WhatToWatch.currMovieID))
        self.numLabel = tk.Label(
            self, text="Number of Movie Reviews: " + num_movie_reviews, fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.numLabel.place(x=65, y=110)

        self.reviews = tk.Text(self, height=5, width=80)
        self.reviews.place(relx=0.5, y=170, anchor=CENTER)
        self.viewMovieReviews()

        self.homeButton = ttk.Button(
            self, text="Done", command=lambda: controller.show_frame("HomePage"))
        self.homeButton.place(relx=0.5, y=550, anchor=CENTER)

    # retrieves reviews for currMovieID, call each time currMovieID is updated
    def viewMovieReviews(self):
        self.reviews.config(state=NORMAL)
        movieID = WhatToWatch.currMovieID
        reviewsList = back.getMovieReviews(movieID)
        # print(reviewsList)
        formattedReviews = ""
        for r in reviewsList:
            formattedReviews = formattedReviews + r
        self.reviews.delete("1.0", END)
        self.reviews.insert(END, formattedReviews)
        self.reviews.config(state=DISABLED)


class ViewUserReviewsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700,
                          height=700, background=darkred)
        self.controller = controller
        label = tk.Label(self, text="Reviews", font=("Helvetica", 40))
        label.pack(side="top", fill="x", pady=10)

        self.userLabel = tk.Label(
            self, text="User ID: " + WhatToWatch.userID, fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.userLabel.place(x=65, y=90)

        num_user_reviews = str(back.getNumUserReviews(WhatToWatch.userID))
        self.numLabel = tk.Label(
            self, text="Number of User Reviews: " + num_user_reviews, fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.numLabel.place(x=65, y=110)

        self.reviews = tk.Text(self, height=5, width=80)
        self.reviews.place(relx=0.5, y=180, anchor=CENTER)
        self.viewUserReviews()

        # Edit Review Label
        self.editLabel = tk.Label(
            self, text="Enter the Review ID, the New Rating, and New Review and Press Enter to Edit Review: ",
            fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.editLabel.place(x=65, y=250, anchor=W)
        self.review_idLabel = tk.Label(
            self, text="Review ID: ", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.review_idLabel.place(x=65, y=265)
        self.review_id = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.review_id.place(x=165, y=265)
        self.ratingLabel = tk.Label(
            self, text="Rating (1-10): ", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.ratingLabel.place(x=65, y=300)
        self.rating = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.rating.place(x=165, y=300)
        self.new_reviewLabel = tk.Label(
            self, text="New Review: ", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.new_reviewLabel.place(x=65, y=345)
        self.new_review = tk.Text(self, height=5, width=60)
        self.new_review.place(x=165, y=345)

        self.searchButton = ttk.Button(
            self, text="Enter", command=self.editReview)
        self.searchButton.place(x=165, y=435, anchor=W)

        self.deleteLabel = tk.Label(
            self, text="Enter the Review ID of the review you want to delete: ",
            fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.deleteLabel.place(x=65, y=475, anchor=W)
        self.delete_idLabel = tk.Label(
            self, text="Review ID: ", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.delete_idLabel.place(x=65, y=500)
        self.delete_id = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.delete_id.place(x=165, y=500)
        self.deleteButton = ttk.Button(
            self, text="Enter", command=self.deleteReview)
        self.deleteButton.place(x=165, y=550, anchor=W)

        self.homeButton = ttk.Button(
            self, text="Done", command=lambda: controller.show_frame("HomePage"))
        self.homeButton.place(relx=0.5, y=585, anchor=CENTER)

    # retrieves reviews for currUserID, call each time currUserID is updated
    def viewUserReviews(self):
        self.reviews.config(state=NORMAL)
        reviewsList = back.getUserReviews(WhatToWatch.userID)
        # print(reviewsList)
        formattedReviews = ""
        for r in reviewsList:
            formattedReviews = formattedReviews + r
        self.reviews.delete("1.0", END)
        self.reviews.insert(END, formattedReviews)
        self.reviews.config(state=DISABLED)

    def editReview(self):
        review_id = self.review_id.get()
        update = self.new_review.get("1.0", END)
        user_id = WhatToWatch.userID
        rating = self.rating.get()
        result = back.editReview(user_id, review_id, update, rating)
        print(result)
        return result

    def deleteReview(self):
        review_id = self.delete_id.get()
        user_id = WhatToWatch.userID
        result = back.deleteReview(review_id, user_id)
        print(result)
        return result


class ViewSearchMovies(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=700,
                          height=700, background=darkred)
        self.controller = controller
        label = tk.Label(self, text="Search", font=("Helvetica", 40))
        label.pack(side="top", fill="x", pady=10)

        self.searchLabel = tk.Label(
            self, text="Search By: ", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.searchLabel.place(x=65, y=90)
        
        v = StringVar()
    
        self.searchTitle = tk.Radiobutton(self, text="Title", variable=v, value="Title",fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.searchTitle.place(x=150, y=90)
        
        self.searchGenre = tk.Radiobutton(self, text="Genre", variable=v, value="Genre", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.searchGenre.place(x=270, y=90)
        
        self.searchAverageRating = tk.Radiobutton(self, text="Avg_rating", variable=v, value="Avg_rating", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.searchAverageRating.place(x=400, y=90)
                
        self.v = v

        num_movie_reviews = str(back.getNumMovieReviews(WhatToWatch.currMovieID))
        self.numLabel = tk.Label(
            self, text="Parameter: ", fg=textcolor, bg=darkred, font=("Helvetica", 15))
        self.numLabel.place(x=65, y=130)
        
        self.paramter = tk.Entry(self, fg=textcolor, bg=darkred, bd=2)
        self.paramter.place(x=150, y=130)
        
        self.searchButton = ttk.Button(self, text="Search", command=self.viewSearchResults)
        self.searchButton.place(x=450, y=140, anchor=CENTER)
        
        self.reviews = tk.Text(self, height=20, width=80)
        self.reviews.place(relx=0.5, y=350, anchor=CENTER)
        #self.viewSearchResults()
        
        

        self.homeButton = ttk.Button(
            self, text="Done", command=lambda: controller.show_frame("HomePage"))
        self.homeButton.place(relx=0.5, y=550, anchor=CENTER)

    # retrieves results for search paramters, call when search is hit
    def viewSearchResults(self):
        print("clicked")
        print(self.v.get()) 
        print(self.paramter.get())
        self.reviews.config(state=NORMAL)
        searchBy = self.v.get()
        searchList = []
        if searchBy == "Title":
            searchList = back.searchTitle(self.paramter.get())
        elif searchBy == "Genre":
            searchList = back.searchGenre(self.paramter.get())
        else:
            searchList = back.searchAvg(self.paramter.get())
        # print(reviewsList)
        formattedSearch = ""
        for s in searchList:
            formattedSearch = formattedSearch + s
        self.reviews.delete("1.0", END)
        self.reviews.insert(END, formattedSearch)
        self.reviews.config(state=DISABLED)


# window.title('WhatToWatch')
# window.geometry("650x650+10+10")
app = WhatToWatch()
app.mainloop()

back.close()
