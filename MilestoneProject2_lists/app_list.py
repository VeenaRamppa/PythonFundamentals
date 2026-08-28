from utils import database_list

USER_CHOICE = """
Enter:
- 'a' to add a book
- 'l' to list all books
- 'r' to read a book
- 'd' to delete a book

Your choice: """

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Please enter a valid input")

        user_input = input("Please enter your choice: ")


def prompt_add_book():
    name = input("Enter the new book name: ")
    author = input("Enter the new book author: ")

    database_list.add_book(name,author)


def list_books():
    books = database_list.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f'{book["name"]} by {book["author"]}, read: {book["read"]}')


def prompt_read_book():
    name = input("Enter the book name to be marked as read: ")

    database_list.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the book name to be marked as delete: ")

    database_list.delete_book(name)

menu()