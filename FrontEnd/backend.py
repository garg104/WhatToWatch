
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
    print("QUERY: " + query)
    try:
        cursor.execute(query)
    except:
        print("Error connecting on retrieve")
        return

    for (userID, username, first_name, last_name, email, password) in cursor:
        globalUserInfo = "userID:" + str(userID) + ", username:" + username + \
            ", first_name:" + first_name + ", last_name:" + last_name + ", email:" + email
    return globalUserInfo


def getUserInfo():
    return globalUserInfo


def close():
    cursor.close()
    cnx.close()
