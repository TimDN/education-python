import sqlite3

def cursor_example():
    try:
        db_connection = sqlite3.connect("test.db")
        cursor = db_connection.cursor()
        cursor.execute("select sqlite_version();")
        record = cursor.fetchall()
        print("SQLite version:",record)
        # prints SQLite version [('3.31.1',)]
        cursor.close()
    finally:
        db_connection.close()

def connect_and_close():
    try:
        # connects to the file test.db and opens it as a database
        db_connection = sqlite3.connect("test.db")
        print(dir(db_connection)) # prints all connect object methods
    finally:
        db_connection.close()

connect_and_close()
cursor_example()