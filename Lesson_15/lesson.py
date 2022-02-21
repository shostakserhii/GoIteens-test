from pprint import pprint

class Student:

    decrease_amount = 0.1
    number_of_students = 0

    def __init__(self, first, last, age, grant):
        self.first = first
        self.last = last
        self.age = age
        self.grant = grant
        self.email = f'{first}.{last}@university.edu'
        Student.number_of_students += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def decrease_grant(self):
        self.grant = float(self.grant - self.decrease_amount)

print(Student.number_of_students)
std_1 = Student('John', 'Wik', 17, 1)
std_2 = Student('Kris', 'Django', 19, 0.9)
print(Student.number_of_students)

# print(std_1.grant)
# std_1.decrease_grant()   #Student.fullname(std_1)
# print(std_1.grant)
#
# print()
# print(std_2.grant)
# print(std_2.__dict__)
#
#
# print(std_2.__dict__)
# std_2.decrease_grant()
# print(std_2.grant)


# print(std_1.__dict__)
# pprint(Student.__dict__)


# print(std_1.grant)
# std_1.decrease_grant()
# print(std_1.grant)
# print(std_1.fullname())
# print(Student.fullname(std_1))

# print(std_1.first)
# print(std_1.last)
# print(std_1.age)
# print(std_1.email)
# print()

# print()
# print(std_2.fullname())
# print(std_2.first)
# print(std_2.last)
# print(std_2.age)
# print(std_2.email)
