"""
In this example implementing the class that hundred number generators

"""

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):     ## all objects which have this __next__() method are called as iterators
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else: # when we reach 100 we have to raise a special error called StopIteration, this error tells python that we have reached end of this generator
            raise StopIteration()


my_gen = FirstHundredGenerator()
print(my_gen.number)
my_gen.__next__()
print(my_gen.number)

## to call it as a generator :
print(next(my_gen))
print(next(my_gen))
