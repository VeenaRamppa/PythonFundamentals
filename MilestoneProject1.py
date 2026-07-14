MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title:{movie['title']}")
    print(f"Director:{movie['director']}")
    print(f"Release year:{movie['year']}")


def search_movie():
    search_title = input("Enter the movie title you're looking for: ")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)
        else:
            print("Movie not found")


user_option = {
    'a': add_movie,
    'l': show_movies,
    'f': search_movie
}

# Below if elif else section is good if we have less number of options like below add, list and find
# If we have more option may be 10 or more then we can use first class functions.
"""
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            show_movies()
        elif selection == 'f':
            search_movie()
        else:
            print("Unknown command. Please try again.")

        selection = input(MENU_PROMPT)
"""


# First class function, user_option dictionary is created to associate the different function with user selection
# and selected option is assigned to a variable which inturn assigned by a function and called with ()a
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_option:
            selected_option = user_option[selection]
            selected_option()
        else:
            print("Unknown command. Please try again.")

        selection = input(MENU_PROMPT)


menu()
