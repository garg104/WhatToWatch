
import mysql.connector

import connection_info

cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                              host=connection_info.MyHost,
                              database=connection_info.MyDatabase)

cursor = cnx.cursor()


userID = None
usrname = raw_input('Enter your username: ')
firstname = raw_input('Enter your first name: ')
lastname = raw_input('Enter your last name: ')
eml = raw_input('Enter your email: ')
psswd = raw_input('Enter your password: ')

query = "Insert INTO Users(userID, username, first_name, last_name, email, password) " \
        "VALUES (%s, %s, %s, %s, %s, %s);"

values = (userID, usrname, firstname, lastname, eml, psswd)

cursor.execute(query, values)
cnx.commit()
print("user inserted")

cursor.close()
cnx.close()
