from utils import database_files_csv

USER_CHOICE = """
Enter
- 'a' to add a book
- 'l' to list all books
- 'r' to read a book
- 'd' to delete a book
- 'q' to quit

Your choice: 

"""

def menu():
    database_files_csv.create_books_table()
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
            print("Invalid choice ")
        user_input = input("Enter your choice:")

def prompt_add_book():
    name = input("Enter a new book name:")
    author = input("Enter a new book author:")

    database_files_csv.add_book(name, author)


def list_all_books():
    books = database_files_csv.get_all_books()
    for book in books:
        read = 'YES' if book["read"] == '1' else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

def prompt_read_book():
    name = input("Enter the book name:")
    database_files_csv.mark_book_read(name)

def prompt_delete_book():
    name = input("Enter the book name you wish to delete:")
    database_files_csv.delete_book(name)



menu()