class Student:
# __init__ is a dundar method, a special/magic method in python
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


    def average(self):
        return sum(self.grade)/ len(self.grade)

student_one = Student("Sara", [70,88,98,59,60])
student_two = Student("Veena", [56,88,67,59,60])

print(student_one.__class__)
print(student_two.__class__)
print(student_one.name)
print(student_one.grade)
print(student_two.name)
print(student_two.grade)

print(student_one.average())
print(student_two.average())
# When you call a class function using class object , Python internally doing like below:
#print(Student.average(student_one))
#print(Student.average(student_two))

#Everything in Python are almost like object
movies = ['Matrix','Finding nemo']
print(movies.__class__) # prints <class 'list'>
print("hi".__class__) # prints <class 'str'>

class Garage:
    def __init__(self):
        self.car = []


    def __len__(self):
        return len(self.car)


    def __getitem__(self,item):
        return self.car[item]

    def __repr__(self):
        return f"<Garage {self.car}>"

    def __str__(self):
        return f"<Garage {self.car}>"

ford = Garage()
ford.car.append("Fiesta")
ford.car.append("Focus")

print(ford.car) # This prints ['Fiesta', 'Focus']

# If we want to find the length of the car , how many cars are in the Garage ford if you use len(ford) it gives error
# TypeError: object of type 'Garage' has no len()
# In order to tell python that this Garage has a length we need to define another dunder method __len__() and it has to return length of the Garage
print(len(ford.car))
# The List class has this __len__() dunder method, hence when len() function is used it returns length of list/tuple/string

# If we try to access/print ford[0], it prints an error as:
# TypeError: 'Garage' object does not support indexing
# We need to define another dunder method to get the indexing values __getitem__()
# it takes self parameter the object on which we are calling and the index that we are trying to access
print(ford[0])   # it is the same calling as Garage.__getitem__(ford)

## when you have __len__() and __getitem__() methods defined in your class , then you can iterate through the object,eg:

for car in ford:
    print(car)

# 2 more magic methods are __repr__() & __str__()
# __repr__() is used to print out the string representing the object

# __str__() is used to return a string that tells the user some information about the class eg Garage
print(ford) # __str__() is used 

