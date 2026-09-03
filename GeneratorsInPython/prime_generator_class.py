class PrimeGenerator:
    def __init__(self,stop):
        self.start = 2
        self.stop = stop

    def __next__(self):
        for n in range(self.start, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                self.start = n+1
                return n
        raise StopIteration()

my_obj = PrimeGenerator(100)
print(my_obj.__next__())
print(my_obj.__next__())
print(my_obj.__next__())
print(my_obj.__next__())
print(my_obj.__next__())
print("#########")
print(next(my_obj))
print(next(my_obj))