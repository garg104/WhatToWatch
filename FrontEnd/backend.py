
import mysql.connector

import connection_info

try:
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)
except:
    print("Error on initial connection")

cursor = cnx.cursor()

globalUserInfo = "default"


def getMovieReviews(movieID):
    # retrieve all reviews associated with specified movie id
    query = "SELECT username, comment, rating FROM Users NATURAL JOIN MovieReviews WHERE movieID = " + movieID + ";"
    #query = "SELECT username, comment, rating FROM Users NATURAL JOIN MovieReviews WHERE movieID = %s;"
    #values = (movieID)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on getting movie reviews")
        return

    reviews = []

    for (username, comment, rating) in cursor:
        review = username + "\nRating: " + \
            str(rating) + " | Comment: " + comment + "\n"
        reviews.append(review)
    return reviews


def getNumMovieReviews(movieID):
    # retrieve number of reviews associated with specified movie id
    args = [movieID, 0]
    result = 0

    try:
        result = cursor.callproc('GetTotalMovieReviews', args)
    except:
        print("Error connecting on getting number of movie reviews")
        return

    return result[1]


def getUserReviews(userID):
    # retrieve all reviews associated with specified user id
    query = "SELECT title, comment, rating, movieID FROM Users NATURAL JOIN MovieReviews NATURAL JOIN Movies WHERE userID = " + userID + ";"
    #query = "SELECT title, comment, rating, movieID FROM Users NATURAL JOIN MovieReviews NATURAL JOIN Movies WHERE userID = %s;"
    #values = (userID)

    try:
        cursor.execute(query)
    except:
        print("Error connecting on getting user reviews")
        return

    reviews = []

    for (username, comment, rating, movieID) in cursor:
        review = username + "\nRating: " + \
            str(rating) + " | Comment: " + comment + "Review ID: " + str(movieID) + "\n\n"
        reviews.append(review)
    return reviews


def getNumUserReviews(userID):
    # retrieve number of reviews associated with specified user id
    args = [userID, 0]
    result = 0

    try:
        result = cursor.callproc('GetTotalUserReviews', args)
    except:
        print("Error connecting on getting number of user reviews")
        return

    return result[1]


def newReview(userID, movieID, rating, comment):
    # insert new review into MovieRevies table
    query = "INSERT INTO MovieReviews(userID, movieID, rating, comment) " \
        "VALUES (%s, %s, %s, %s);"

    values = (userID, movieID, rating, comment)

    try:
        cursor.execute(query, values)
    except:
        print("Error connecting on insert new review")
    cnx.commit()
    print("review inserted")

    # update avg_rating value for movie that was just reviewed
    query0 = "SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;"
    try:
        cursor.execute(query0)
    except:
        print("Error connecting on update avg_rating1")
        return
    query0 = "START TRANSACTION;"
    try:
        cursor.execute(query0)
    except:
        print("Error connecting on update avg_rating2")
        return
    query = "UPDATE Movies SET avg_rating = (SELECT AVG(rating) FROM MovieReviews WHERE movieID = " + \
        movieID + ") WHERE movieID = " + movieID + ";"
    #query = "UPDATE Movies SET avg_rating = (SELECT AVG(rating) FROM MovieReviews WHERE movieID = " \
    #        "%s) WHERE movieID = %s;"
    #values = (int(movieID), int(movieID))
    print(query)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on update avg_rating3")
        return
    query0 = "COMMIT;"
    try:
        cursor.execute(query0)
    except:
        print("Error connecting on update avg_rating4")
        return
    cnx.commit()
    print("avg updated")


def insert(userID, usrname, firstname, lastname, eml, psswd):
    
    #query0 = "SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;"
    #try:
    #    cursor.execute(query0)
    #except:
    #    print("Error connecting on update avg_rating1")
    #    return
    query = "Insert INTO Users(userID, username, first_name, last_name, email, password) " \
        "VALUES (%s, %s, %s, %s, %s, %s);"

    values = (userID, usrname, firstname, lastname, eml, psswd)

    try:
        cursor.execute(query, values)
    except:
        print("Error connecting on insert")
    cnx.commit()
    print("user inserted")
    
    
def retrieve(usrname):
    #query = "SELECT * FROM Users WHERE username = '" + usrname + "';"
    query = "SELECT * FROM Users WHERE username = %s;"
    values = (usrname)
    #print("QUERY: " + query)
    try:
        cursor.execute(query, values)
    except:
        print("Error connecting on retrieve user info")
        return

    for (userID, username, first_name, last_name, email, password) in cursor:
        globalUserInfo = "userID:" + str(userID) + ", username:" + username + \
            ", first_name:" + first_name + ", last_name:" + last_name + ", email:" + email
    return globalUserInfo


def searchTitle(title):
    #query = "SELECT * FROM Movies WHERE Title = '" + title + "';"
    query = "SELECT * FROM Movies WHERE Title = %s;"
    values = (title)
    print("QUERY1: " + query, title)
    try:
        cursor.execute(query, title)
    except:
        print("Error connecting on retrieve user info")
        return
    
    results = []

    for (m_id, c_title, c_year, c_duration, c_genre, c_desciption, c_avg_rating) in cursor:
        result = "ID: " + str(m_id) + "| title:" + c_title + "| year:" + str(c_year) + \
            "| duration:" + str(c_duration) + "| genre:" + c_genre + "| description:" + c_desciption + "| avg_rating:" + str(c_avg_rating) + "\n\n"
        results.append(result)
    return results


def searchGenre(genre):
    #query = "SELECT * FROM Movies WHERE Genre = '" + genre + "';"
    query = "SELECT * FROM Movies WHERE Genre = %s;"
    values = (genre)
    print("QUERY2: " + query)
    try:
        cursor.execute(query, values)
    except:
        print("Error connecting on retrieve user info")
        return
    
    results = []

    for (m_id, c_title, c_year, c_duration, c_genre, c_desciption, c_avg_rating) in cursor:
        result = "ID: " + str(m_id) + "| title:" + c_title + "| year:" + str(c_year) + \
            "| duration:" + str(c_duration) + "| genre:" + c_genre + "| description:" + c_desciption + "| avg_rating:" + str(c_avg_rating) + "\n\n"
        results.append(result)
    return results


def searchAvg(avg_rating):
    query = "SELECT * FROM Movies WHERE avg_rating >= '" + avg_rating + "';"
    print("QUERY3: " + query)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on retrieve user info")
        return
    
    results = []

    for (m_id, c_title, c_year, c_duration, c_genre, c_desciption, c_avg_rating) in cursor:
        result = "ID: " + str(m_id) + "| title:" + c_title + "| year:" + str(c_year) + \
            "| duration:" + str(c_duration) + "| genre:" + c_genre + "| description:" + c_desciption + "| avg_rating:" + str(c_avg_rating) + "\n\n"
        results.append(result)
    return results


def deleteUser(user_id):
    query = "DELETE FROM MovieReviews WHERE userID = " + user_id + ";"
    #values = (user_id)
    print("QUERY: " + query)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on retrieve user info")
        return
    
    cnx.commit()

    query = "DELETE FROM Users WHERE userID = " + user_id +";"
    #values = (int(user_id))
    print("QUERY: " + query)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on retrieve user info")
        return
    
    cnx.commit()
    return "success"


def editReview(user_id, review_id, update, rating):
    #update = update + "\n"
    query = "UPDATE MovieReviews SET comment = %s, rating = %s" \
            " WHERE userID = %s AND movieID = %s;"
    values = (update, str(rating), user_id, review_id)
    print(query, values)
    try:
        cursor.execute(query, values)
    except:
        print("Error connecting on edit review")
        return

    cnx.commit()
    return "success"

def deleteReview(movie_id, user_id):
    query = "DELETE FROM MovieReviews WHERE movieID = %s AND userID = %s;"
    values = (movie_id, user_id)
    print(query)
    try:
        cursor.execute(query, values)
    except:
        print("Error connecting on Delete Review")
        return

    cnx.commit()

    query = "UPDATE Movies SET avg_rating = (SELECT AVG(rating) FROM MovieReviews WHERE movieID = " \
            "%s) WHERE movieID = %s;"
    values = (movie_id, movie_id)
    print(query)
    try:
        cursor.execute(query, values)
    except:
        print("Error updating average on Delete Review")
        return
    cnx.commit()
    return "success"

def login(user, pswrd):
    query = "SELECT userID FROM Users WHERE username = %s AND password = %s;"
    values = (user, pswrd)
    print(query)
    try:
        cursor.execute(query, values)
    except:
        print("Error logging in")
        return
    records = cursor.fetchall()
    for row in records:
        id = row[0]
    #print(id)

    return id


def getUserInfo():
    return globalUserInfo


def close():
    cursor.close()
    cnx.close()
