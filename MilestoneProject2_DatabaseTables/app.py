from utils import database

USER_CHOICE = """
Enter 
- 'a' to add a book
- 'l' to list all books
- 'r' to update the read status
- 'd' to delete a book
- 'q' to quit

Your choice: 
"""

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_all_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Invalid choice")

        user_input = input("Enter your choice: ")


def prompt_add_book():
    name = input("Enter a new book name: ")
    author = input("Enter the author: ")
    database.add_book(name, author)


def list_all_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read:{read}")


def prompt_read_book():
    name = input("Enter a book name which you want to mark it as read: ")
    database.mark_book_as_read(name)

def prompt_delete_book():
    name = input("Enter the name of the book you wish to delete: ")
    database.delete_book(name)


menu()


