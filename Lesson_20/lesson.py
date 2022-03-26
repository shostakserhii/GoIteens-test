
class Employee: #emp_1

    increase_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):    #initialize
        self.first = first   # emp_1.first = 'Volodya'
        self.last = last     # emp_1.last = 'Zelenskiy'
        self.pay = pay
        self.email = f'{first}.{last}@company.ua'
        Employee.number_of_employees += 1

    def __str__(self):
        return f"{self.last} {self.first}, email: {self.email}, sallary: {self.pay}"

    def __repr__(self):
        return f"{self.last} {self.first}, email: {self.email}, sallary: {self.pay}"

    def fullname(self):
        return f'{self.first} {self.last}'

    def pay_increase(self):
        self.pay *= self.increase_amount


emp_1 = Employee('Volodya', 'Zelenskiy', 50000)
emp_2 = Employee('Test', 'User', 60000)


from datetime import date
date_today = date.today()
print(date_today)
print(str(date_today))
print(repr(date_today))
# print(emp_1.__dict__)
# print(emp_2.__dict__)
# print()
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))
# print()
# print(emp_2.fullname())
# print(Employee.increase_amount)
# print(emp_1.pay)
# emp_1.increase_amount = 2
# print(emp_1.__dict__)
# emp_1.pay_increase()
# print(int(emp_1.pay))
# print(Employee.number_of_employees)
# emp_2 = Employee('Test', 'User', 60000)
# print(Employee.number_of_employees)
list_1 = ['a', 'c', 'c']
print(list_1)
print(type(list_1))
print(emp_1)
print(emp_1)
employees = []
employees.append(emp_1)
employees.append(emp_2)
print(employees)