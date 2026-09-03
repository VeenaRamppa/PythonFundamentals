"""
Generator in Python is a function, its a special function that remembers the state its in inbetween executions.
You can run the function multiple time and it will remember what it did last time that you ran it.

"""

def prime_generator(bound):
    for n in range(2,bound):
        for x in range(2,n):
            if n%x == 0:
                break
        else:
            yield n


g = (prime_generator(20))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
