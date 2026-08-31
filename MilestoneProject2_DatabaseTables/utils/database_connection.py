import sqlite3
"""
Context Manager in Python
    with ... as ...
        pass
    Above statements is something called as context manager. By context what we mean that the current status of the application
    at the point in which this blocks runs(with ... as ...), is modified  by this (pass) that its controlled by the statement(with ... as ...)

    (with ... as ...) this modifies the status or the context when you fo in, and it also modifies it when you go out.
    That allows you to do some setup when you start and some teardown when you end.

    We can create our own context managers , by set up statements like :
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
    And tear down lines like :
        connection.commit()
        connection.close()
    This shows that pretty idea of using the context manager , so instead of writing the same code for each function we can use
    context managers
    Let's do the context managers for our datanase connection so that no need to open and close the connection every time

    To create a context manager, we need to create a new python file and create a class DatabaseConnection
    In order to use the class as a context manager we need two dunder methods __enter__(self) & __exit__(self,exc_type,exc_value,traceback))
    
    __enter__() method is called as you enter the context manager and 
    __exit__() method is called as you leave the context manager. This has 3 values for exception, exc_type, exc_value and exception traceback
    During the execution of a context manager error may occur , SQLite may raise an error b4 program crashes it will go to the exit method
    If no error occurs all the 3 parameters have None value.
    
    We should do sqlite3.connect() inside __enter__() method 
    We should do connection.commit() , connection.close() in __exit__() method


"""

class DatabaseConnection:
    def __init__(self,host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type or exc_value or traceback:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()

