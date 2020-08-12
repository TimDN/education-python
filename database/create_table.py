import sqlite3

def create_table(cursor):
    create_student_table = """ CREATE TABLE IF NOT EXISTS student (
                            id integer PRIMARY KEY,
                            name text NOT NULL
                        ) """
    cursor.execute(create_student_table)
    # creates table with attributes id and name


def insert_student(cursor, connection, name):
    insert_student_query = "INSERT INTO student VALUES (null, ?)"
    cursor.execute(insert_student_query, [name])
    connection.commit()

def get_students_with_name(cursor, name):
    get_students_query = "SELECT * FROM student WHERE name = ?"
    cursor.execute(get_students_query, [name])
    result = cursor.fetchall()
    print(result)

def update_student_name(cursor, connection, new_name, old_name):
    update_name_query = "UPDATE student SET name = ? WHERE name = ?"
    cursor.execute(update_name_query, [new_name, old_name])
    connection.commit()

def delete_students_with_name(cursor, connection, name):
    delete_student_query = "DELETE FROM student WHERE name = ?"
    cursor.execute(delete_student_query, [name])
    connection.commit()

def delete_table(cursor, connection, table_name):
    drop_table_query = "DROP TABLE IF EXISTS student"
    cursor.execute(drop_table_query)
    connection.commit()

try:
    db_connection = sqlite3.connect("school.db")
    cursor = db_connection.cursor()
    create_table(cursor)
    insert_student(cursor, db_connection, "Foo")
    get_students_with_name(cursor, "Foo")
    update_student_name(cursor, db_connection, "Bar", "Foo")
    get_students_with_name(cursor, "Bar")
    delete_students_with_name(cursor, db_connection, "Bar")
    delete_table(cursor, db_connection, "student")
    cursor.close()
finally:
    db_connection.close()

