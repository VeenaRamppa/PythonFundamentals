import json
"""
Concerned with updating and retrieving the book names from a json file

json structure:
[
    {
        "name" : name,
        "author": author,
        "read": True
    }
]
"""

book_files = "books.json"

def create_book_table():
    with open(book_files, 'w') as file :
        # pass # it  requires json to be dump with empty list inorder avoid json.decoder error
        json.dump([],file)

def add_book(name, author):
    books = get_all_book()
    books.append({'name': name, 'author': author, 'read':False})
    _save_all_books(books)

def get_all_book():
    with open(book_files, 'r') as file:
        return json.load(file)

def _save_all_books(books):
    with open(books,'w') as file:
        json.dump(books,file)

def mark_book_as_read(book_name):
    books = get_all_book()
    for book in books:
        if book['name'] == book_name:
            book['read'] = True
    _save_all_books(books)

def delete_book(name):
    books = get_all_book()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)



