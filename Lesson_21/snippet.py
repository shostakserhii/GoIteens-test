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
        return f"{self.last} {self.first}, email: {self.email}, sallary: {self.pay}"

    def fullname(self):
        return f'{self.first} {self.last}'

    def pay_increase(self):
        self.pay *= self.increase_amount

##############################################################################
# class Developer(Employee):
#     pass
# dev_1 = Developer('Serhii', 'Shostak', 50000)
# dev_2 = Developer('Eney','Parubok', 60000)
# print(dev_1.email)
# print(help(Developer))
# ##############################################################################
# class Developer(Employee):
#     increase_amount = 1.1
# dev_1.pay
# dev_1.increase_amount()
# dev_1.pay
##############################################################################
class Developer(Employee):
    increase_amount = 1.1

    def __init__(self, first, last, pay, programming_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.programming_lang = programming_lang

dev_1 = Developer('Serhii', 'Shostak', 50000, 'Python')
dev_2 = Developer('Eney','Parubok', 60000, 'C++')
dev_1.email
dev_1.programming_lang
##############################################################################
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees:
            self.employees = employees
        else:
            self.employees = []

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.append(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())

mng_1 = Manager('A','S',40000,[dev_1])
print(mng_1.email)
mng_1.print_emps()
################################################################################
print(isinstance(mng_1, Manager))
print(isinstance(mng_1, Employee))
print(isinstance(mng_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
################################################################################
Exception