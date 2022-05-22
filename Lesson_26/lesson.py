
x = 2
y = 3
print(pow(x, y))


def own_pow(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result


print(own_pow(2, 3))

bankomat = Bankomat()
bankaccount = BankAccount()

def checkbalance(self, bankaccount):
    bankaccount.show_balance_even_if_private()

bankomat.checkbalance(bankaccount)
