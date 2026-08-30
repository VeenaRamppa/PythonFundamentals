import sqlite3

"""
Concerned with storing and retrieving books from a database
"""

def create_book_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE books(name text primary key,author text,read integer)')
    connection.commit()
    connection.close()

def add_book(name,author):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
# Actually we have not written anything to the database, nothing save to the disc just read from the database so commit() is not required
    #connection.commit()

# fetchall() gives a list of tuples[(name,author,read_status),(name,author,read_status)], we can read each value based on index
# OR
# we can directly convert them to dictionaries and easy to use in our program and good way was using data structures
    books = [{'name':row[0],'author':row[1],'read':row[2] } for row in cursor.fetchall()]
    connection.close()
    return books


def mark_book_as_read(book):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET read = 1 WHERE name=?",(book,)) # you must not use the attribute name or variable,fstrings in the
    # SQL query like WHERE name=book, this will lead to potential SQL injection attacks, instead supply the value through
    # a tuple like (book,)
    connection.commit()
    connection.close()

def delete_book(book):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE name=?",(book,))
    connection.commit()
    connection.close()

