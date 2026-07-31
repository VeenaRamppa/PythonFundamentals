class Student(self,name,school):
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []


    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary
    @property
    def weekly_salary(self):
        return self.salary * 40

rolf = WorkingStudent('Rolf','LTH',200)
print(rolf.salary)
rolf.marks.append(50)
rolf.marks.append(70)
print(rolf.average())
print(rolf.weekly_salar)

anna = Student('Anna','LTH')
# anna.weekly_salary() ## This line generates an error AttributeError: 'student' object has no attribute 'weekly_salary'
# Bcoz weekly_salary() is defined in WorkingStudent class .

### Decorator @property
## When a function is just taking the self as an argument and its operation is to just some calculation
## eg. weekly_salary() . It is just calculating the value and returning it.
## You can use @property decorator and inform python that this function is just used for the purpose of calculation
# and there are no actions like connecting to database , calling other function etc.
# then you can call this function without () and say that this function is a object's property
print(rolf.weekly_salary)

