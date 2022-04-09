
"""
IF
"""

# x = input('Enter message: ')
#
# if x.isalpha():
#     print(f'"{x}" is str')
#     print(x + '_hello')
# elif x.isdigit():
#     print(f'{x} is digit')
#     print(int(x)**int(x))
# elif x.isalnum():
#     print(f'{x} has both digits and letters')
# else:
#     print('no check returned True')
#
# print('bye')

# True, 1, "hello"
# False, 0, None, ""
#
# msg = ''
#
# if not msg:  #not False = True
#     print('It\'s empty of False!')

print('welcome to calc')
operation = input("""
You can choose + or -
Type here: """)

if operation == '+':
    first = input('Enter first number: ')
    if first.isdigit():
        second = input('Enter second number: ')
        if second.isdigit():
            print(f'{first} + {second} = {int(first) + int(second)}')
        else:
            print(f'{second} is not digit')
    else:
        print(f'{first} is not digit')
elif operation == '-':
    first = input('Enter first number: ')
    if first.isdigit():
        second = input('Enter second number: ')
        if second.isdigit():
            print(f'{first} - {second} = {int(first) - int(second)}')
        else:
            print(f'{second} is not digit')
    else:
        print(f'{first} is not digit')
else:
    print(f'{operation}: Sorry, not supported')
