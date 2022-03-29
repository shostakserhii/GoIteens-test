
class Employee:

    increase_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.ua'
        Employee.number_of_employees += 1

    def __str__(self):
        return f"{self.last} {self.first}, email: {self.email}, sallary: {self.pay}"

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"        #<---------------------------------------------

    # def __add__(self, other):
    #     return self.pay + other.pay
    #
    # def __len__(self):
    #     return len(self.fullname())

    def fullname(self):
        return f'{self.first} {self.last}'

    def pay_increase(self):
        self.pay *= self.increase_amount

emp_1 = Employee('AAA', 'BBBB', 50000)
emp_2 = Employee('CCCC', 'DDDDD', 60000)
print(emp_1)

########################################################################################################################
# print(1 + 2)
# print('a' + 'b')
# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))
# print(emp_1+emp_2) #TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'
#
# print(len('test'))
# print('test'.__len__())
# print(len(emp_1))



