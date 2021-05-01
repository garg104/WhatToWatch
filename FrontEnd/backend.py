
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
    query = "SELECT title, comment, rating FROM Users NATURAL JOIN MovieReviews NATURAL JOIN Movies WHERE userID = " + userID + ";"

    try:
        cursor.execute(query)
    except:
        print("Error connecting on getting user reviews")
        return

    reviews = []

    for (username, comment, rating) in cursor:
        review = username + "\nRating: " + \
            str(rating) + " | Comment: " + comment + "\n"
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
    query = "UPDATE Movies SET avg_rating = (SELECT AVG(rating) FROM MovieReviews WHERE movieID = " + \
        movieID + ") WHERE movieID = " + movieID + ";"
    try:
        cursor.execute(query)
    except:
        print("Error connecting on update avg_rating")
        return
    cnx.commit()
    print("avg updated")


def insert(userID, usrname, firstname, lastname, eml, psswd):
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
    query = "SELECT * FROM Users WHERE username = '" + usrname + "';"
    #print("QUERY: " + query)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on retrieve user info")
        return

    for (userID, username, first_name, last_name, email, password) in cursor:
        globalUserInfo = "userID:" + str(userID) + ", username:" + username + \
            ", first_name:" + first_name + ", last_name:" + last_name + ", email:" + email
    return globalUserInfo


def deleteUser(usrname):
    # delete the user from the database
    # 1 - go through all the movie reviews and update the avergar rating of the movies
    # 2 - drop the movie reviews table for the user_id
    # 3 - delete the user fromt he users table
    
    query = "SELECT * FROM Users WHERE username = '" + usrname + "';"
    #print("QUERY: " + query)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on retrieve user info")
        return

    for (userID, username, first_name, last_name, email, password) in cursor:
        globalUserInfo = "userID:" + str(userID) + ", username:" + username + \
            ", first_name:" + first_name + ", last_name:" + last_name + ", email:" + email
    return globalUserInfo


def searchTitle(title):
    query = "SELECT * FROM Movies WHERE Title = '" + title + "';"
    print("QUERY1: " + query)
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


def searchGenre(genre):
    query = "SELECT * FROM Movies WHERE Genre = '" + genre + "';"
    print("QUERY2: " + query)
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
    query = "DELETE FROM MovieReviews WHERE userID = " + user_id +";"
    print("QUERY: " + query)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on retrieve user info")
        return
    
    cnx.commit()

    query = "DELETE FROM Users WHERE userID = " + user_id +";"
    print("QUERY: " + query)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on retrieve user info")
        return
    
    cnx.commit()
    return "success"

def getUserInfo():
    return globalUserInfo


def close():
    cursor.close()
    cnx.close()
