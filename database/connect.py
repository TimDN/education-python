import sqlite3

def cursor_example():
    try:
        db_connection = sqlite3.connect("test.db")
        cursor = db_connection.cursor()
        cursor.execute("select sqlite_version();")
        record = cursor.fetchall()
        print("SQLite version:",record)
        # prints SQLite version [('3.31.1',)]
    finally:
        cursor.close()
        db_connection.close()

def connect_and_close():
    try:
        # connects to the file test.db and opens it as a database
        db_connection = sqlite3.connect("test.db")
        print(dir(db_connection)) # prints all connect object methods
    finally:
        db_connection.close()


def unique_test():
    db_connection = sqlite3.connect("unique.db")
    cursor = db_connection.cursor()
    create_student_table = """ CREATE TABLE IF NOT EXISTS student (
                            id integer PRIMARY KEY,
                            name text NOT NULL UNIQUE,
                            age integer UNIQUE
                        ) """
    cursor.execute(create_student_table)
    insert_student = "INSERT INTO student (id, name) VALUES (null, ?)"
    cursor.execute(insert_student, ["foo"])
    db_connection.commit()
    cursor.execute(insert_student, ["foo"])
    db_connection.commit()