"""
Concerned with storing and retrieving books from a csv file.
Format of the csv file:

name,author,read\n
"""
books_file = "books.txt"

def create_books_table():
    with open(books_file, 'w') :
        pass

def add_book(name,author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')

def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]  # [[name,author,read],[name,author,read],[name,author,read]]

    return [
        {'name':line[0],'author':line[1],'read':line[2] }
        for line in lines
    ]


def mark_book_read(book_name):
    books = get_all_books()
    for book in books:
        if book['name'] == book_name:
            book['read'] = '1'
    _save_all_books(books) # why this function is named as _ is bcoz it tells the other developer not to call it , only this function should call this function
    # this is normally known as private function


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")

def delete_book(book_name):
    books = get_all_books()
    books = [book for book in books if book['name'] != book_name]
    _save_all_books(books)