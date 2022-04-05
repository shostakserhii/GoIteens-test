class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property   #getter
    def fullname(self):
        return f'{self.first} {self.last}'

    @property   #getter
    def email(self):
        return f'{self.first}_{self.last}@company.ua'

    @fullname.setter    #setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter   #deleter
    def fullname(self):
        print('Deleting fullname')
        self.first = None
        self.last = None


emp_1 = Employee('Test', 'User', 4000)
emp_1.first = 'Johny'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()
emp_1.fullname = 'John Kelvin'
print(emp_1.first)
print(emp_1.last)

del emp_1.fullname
print(emp_1.first)
print(emp_1.last)
