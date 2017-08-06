from abc import *

# inheritance

# SchoolMember
# абстрактний клас - metaclass=ABCMeta
class SchoolMember(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Create SchoolMember')

    @abstractmethod
    def tell(self):
        '''Write information'''
        print('Name: {0}, age:{1}'.format(self.name, self.age), end=' ')

# Teacher
class Teacher(SchoolMember):
    '''Teacher class'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Create teacher: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: %d UAN\n' % self.salary)

# Student
class Student(SchoolMember):
    '''Student class'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Create student: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: %d\n' % self.marks)

t = Teacher('Mr. Mik', 38, 4400*12)
s = Student('Michael', 21, 87)

print()
members = [t, s]
for m in members:
    m.tell()
