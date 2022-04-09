
"""
Public Access
Protected Access
Private Access
"""


class BankAccount:
    bank_name = "MonoBank"

    def __init__(self, name, passport, pin, balance=0):
        self.__name = name
        self.__passport = passport
        self.__pin = pin
        self.__balance = balance

    def __print_private_account_details(self):
            return(self.__name, self.__passport, self.__pin, self.__balance)

    def check_private_details(self):
        pin = input("Pin: ")
        if self.__pin == int(pin):
            self.print_private_account_details()
        return('Wrong pin!')

    def change_pin_code(self):
        pin = input("Pin: ")
        if self.__pin == int(pin):
            self.__pin == pin

account_1 = BankAccount('User', 32435656, 5785, balance= 10000)

# print(account_1.check_private_details())
print(dir(BankAccount))
print(account_1._BankAccount__print_private_account_details())
#
# print(account_1.__print_private_account_details())

print(account_1._BankAccount__name)

"""
Наслідування
Поліморфізм
Інкапсулація

Абстракція
"""

