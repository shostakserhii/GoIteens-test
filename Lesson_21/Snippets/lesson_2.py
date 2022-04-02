lass Employee:
    increase_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.ua'
        Employee.number_of_employees += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def pay_increase(self):
        self.pay *= self.increase_amount

    def __str__(self):
        return f"{self.last} {self.first}, email: {self.email}, sallary: {self.pay}"

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee('Eney', 'Motornyu', 30000)

class Developer(Employee):
    increase_amount = 1.1
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer('Serh', 'Shos', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

# print(emp_1.increase_amount)
# print(dev_1.increase_amount)

class Manager(Employee):
    increase_amount = 1.3

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay)
        if employees:
            self.employees = employees
        else:
            self.employees = []

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"--->{emp.fullname()}")

    def transfer_to_developer(self):
        return Developer(self.first, self.last, self.pay, 'C++')

mng_1 = Manager('Farik', 'Controller', 30000, [dev_1, dev_2])
# mng_1.add_emp(dev_1)
# mng_1.add_emp(dev_2)
mng_1.rem_emp(dev_2)
mng_1.print_emps()
# print(help(mng_1))
print(isinstance(mng_1, Manager))
print(isinstance(mng_1, Employee))
print(isinstance(mng_1, Developer))
print()
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
print(issubclass(Developer, Employee))

dev_3 = mng_1.transfer_to_developer()
print(dev_3.prog_lang)
