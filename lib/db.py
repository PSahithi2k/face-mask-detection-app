import sqlite3 as lite

# connect to the database
def connect(database_name):
    try:
        connection = lite.connect(database_name)
        return connection
    except lite.Error as error:
        print("Error while connecting to sqlite", error)

# print sqlite version
def version(connection):
    try:
        cursor = connection.cursor()
        query = "select sqlite_version();"
        cursor.execute(query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()
    except lite.Error as error:
        print("Failed to print database version", error)

# insert one record into table
def insert(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Successfully inserted one record")
        cursor.close()
    except lite.Error as error:
        print("Failed to insert data into  table", error)

# fetch all records from table
def fetchall(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except lite.Error as error:
        print("Failed to fetch records the data from table", error)

# fetch one record from table
def fetchone(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        record = cursor.fetchone()
        cursor.close()
        return record
    except lite.Error as error:
        print("Failed to fetch one record from table", error)

# update one record in the table
def update(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Successfully updated one record")
    except lite.Error as error:
        print("Failed to update data into table", error)

# delete one record from table
def delete(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Successfully deleted one record")
    except lite.Error as error:
        print("Failed to delete one record ", error)

# close the connection
def close(connection):
    connection.close()
