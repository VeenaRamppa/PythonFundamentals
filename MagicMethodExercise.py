'''
This time, we have a class defined as such:

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
The Club class represents a sports club, it has a name and a list of players playing for that club.

In this exercise, we will let you design the architecture and inner methods of the Club class. And your goal is to implement the proper methods so that others can interact with this class as follows:

1. You should be able to create an instance of Club like this:

some_club = Club('Arsenal')
2. You should be able to add players to the object my_club like this:

my_club.players.append('Rolf')
my_club.players.append('Anne')
3. You should be able to access the i-th player in my_club like this (assuming that i  is always valid):

my_club[i]
4. At last, you will need to make a decision! You will need to define two methods that do the following work:

One of them should return a string representation of the current object, so that it can be used by others to recreate this object using the string. The return value (taking my_club as example) should look like this:

Club Arsenal: ['Rolf', 'Anne']
The other should return a readable string to the user about this object. The return value should look like this:

Club Arsenal with 2 players

'''

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)

    def __getitem__(self, item):
        return self.players[item]

    def __repr__(self):
        return f'Club {self.name}: {self.players}'

    def __str__(self):
        return f'Club {self.name}: {self.players}'

myclub = Club('Arsenal')
myclub.players = ['Rolf', 'Anne']
print(myclub[0])

