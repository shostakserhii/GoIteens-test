import datetime


class Employee:

    num_of_emps = 0
    raise_amt = 1.04
    company_name = 'Walter White (c)'

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay_per_hour = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def change_company_name(cls, name):
        if name.isalpha():
            cls.company_name = name
        elif name.isdigit():
            print("We are not changing company name to digits!")

    def add_double_pay_for_weekend(self):
        today = datetime.datetime.today()
        print(today)
        if not Employee.is_workday(today):
            self.pay_per_hour *= 2

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Rafik', 'Bayraktar', 15)
print(emp_1.raise_amt)

emp_1.fullname()

Employee.company_name = "dawd"
Employee.change_company_name('LoTR') #Employee.change_company_name(Employee, ('LoTR (c)'))

print(Employee.company_name)

my_date_1 = datetime.date(2022, 5, 20)
print(Employee.is_workday(my_date_1))


print(emp_1.pay_per_hour)
emp_1.add_double_pay_for_weekend()
print(emp_1.pay_per_hour)

