# class Employee:
#     increase_amount = 1.04
#     number_of_employees = 0
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         Employee.number_of_employees += 1
#
#     # @property
#     # def email(self):
#     #     return f'{self.first}.{self.last}@company.ua'
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
# emp_1 = Employee('Serhii', 'Shostak', 50000)
# emp_2 = Employee('Eney','Parubok', 60000)
# emp_1.first = 'Honey'
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())
########################################################################################
class Employee:
    increase_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.number_of_employees += 1

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.ua'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('Serhii', 'Shostak', 50000)
emp_2 = Employee('Eney','Parubok', 60000)
emp_1.first = 'Honey'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'Abra Kadabra'
