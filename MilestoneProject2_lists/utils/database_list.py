"""
Concerned with storing and retrieving books from a list
"""

books = []

def add_book(name, author):
    books.append({
        "name": name,
        "author": author,
        "read":False
    })


def get_all_books():
    return books


def mark_book_as_read(book_name):
    for book in books:
        if book["name"] == book_name:
            book["read"] = True


def delete_book(name):
# Below one is the bad pratice , bcoz as you go/iterate over a list and removing the elements confuses python
#    for book in books:
#        if book["name"] == name:
#            books.remove(book)
    global books
    books = [book for book in books if book['name'] != name] # add each book to a new list if the book['name'] != name
