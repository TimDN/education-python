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
    name = "Foo"
    get_students_query = "SELECT * FROM student WHERE name = ?"
    cursor.execute(get_students_query, [name])
    result = cursor.fetchall() # returns all rows in a list
    print(result) # prints [(1, 'Foo')]

def get_student_name(cursor, id):
    id = "1" # must be of str type
    get_student_name_query = "SELECT name FROM student WHERE id = ?"
    cursor.execute(get_student_name_query, [id])
    result = cursor.fetchone() # returns a row
    print(result) # prints ('Foo',)


def update_student_name(cursor, connection, new_name, old_name):
    new_name = "Bar"
    old_name = "Foo"
    update_name_query = "UPDATE student SET name = ? WHERE name = ?"
    cursor.execute(update_name_query, [new_name, old_name])
    connection.commit()


def delete_students_with_name(cursor, connection, name):
    name = "Bar"
    delete_student_query = "DELETE FROM student WHERE name = ?"
    cursor.execute(delete_student_query, [name])
    connection.commit()


def delete_table(cursor, connection, table_name):
    table_name = "student"
    drop_table_query = "DROP TABLE IF EXISTS {}".format(table_name)
    cursor.execute(drop_table_query)
    # can't use param substition since we only have tables
    connection.commit()

def school_demo():
    try:
        db_connection = sqlite3.connect("school.db")
        cursor = db_connection.cursor()
        create_table(cursor)
        insert_student(cursor, db_connection, "Foo")
        get_students_with_name(cursor, "Foo")
        get_student_name(cursor, 1)
        update_student_name(cursor, db_connection, "Bar", "Foo")
        delete_students_with_name(cursor, db_connection, "Bar")
        delete_table(cursor, db_connection, "student")
        cursor.close()
    finally:
        db_connection.close()

def chinook_or_and_example(cursor):
    get_acdc_and_metallica = """SELECT * FROM artist
                        WHERE Name = 'AC/DC' OR Name = 'Metallica'"""
    cursor.execute(get_acdc_and_metallica)
    result = cursor.fetchall()
    print(result) # prints [(1, 'AC/DC'), (50, 'Metallica')]

def chinook_like_example(cursor):
    #Selects all artists starting with an A
    get_all_artist_starting_with_a = """SELECT * FROM artist
                                    WHERE Name LIKE 'A%'"""
    cursor.execute(get_all_artist_starting_with_a)
    result = cursor.fetchall()
    print(result) # prints (1, 'AC/DC'), (2, 'Accept'), and more

def chinook_order_example(cursor):
    get_artist_starting_with_a_ordered = """SELECT * FROM artist
                                        WHERE Name LIKE 'A%'
                                        ORDER BY Name DESC"""
    # when ordering text DESC it will sort Z to A
    cursor.execute(get_artist_starting_with_a_ordered)
    result = cursor.fetchall()
    print(result) # prints [(26, 'Azymuth'), (166, 'Avril Lavigne'), and more


def chinook_demo():
    try:
        db_connection = sqlite3.connect("Chinook.db")
        cursor = db_connection.cursor()
        chinook_or_and_example(cursor)
        chinook_like_example(cursor)
        chinook_order_example(cursor)
    finally:
        db_connection.close()


chinook_demo()