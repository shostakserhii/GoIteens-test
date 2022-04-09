class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport
    #
    # def print_data(self):
    #     print(self.name, self.balance, self.passport)
    def print_public_data(self):
        self.__private_method()

    def _hi_there(self):
        print('hi')

    def __hi_there(self):
        print('hi there')

    def __private_method(self):
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('lola', 10000, 23124324)
# account1.print_data()
print(dir(account1))
account1.print_public_data()
# print(account1._name)
# print(account1._balance)
# print(account1._passport)

class A(BankAccount):
    pass
a = A('name', 'balance', 'passport')
print(dir(a))

a._hi_there()
