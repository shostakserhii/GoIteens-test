"""
IS
ELIF
ELSE
True == 1, bool(1), not empty value
False == 0, bool(0), empty value
"""

# x = input("Enter number: ")
#
# if x.isalpha():
#     print(f"{x} is alpha")
# elif x.isdigit():
#     print(f"{x} is digit")
# elif x:
#     print(f"{x} not None section!")
# else:
#     print("It's no digit or alpha")
#
# string_number = input("Enter number: ")
#
# if string_number.isdigit() or string_number.isalpha():
#     print(string_number)
# else:
#     print("Not letter or digit")

print("Welcome to Calc!")
operation = input("""
We have few options: + - * /
Choose the one you like: """)
if operation == '+':
    first_number = input("Enter first value: ")
    if first_number.isdigit():
        second_number = input("Second value: ")
        if second_number.isdigit():
            print(f"{first_number} + {second_number} = {int(first_number) + int(second_number)}")
        else:
            print(f"{second_number} is not digit")
    elif first_number.isalpha():
        second_number = input("Second value: ")
        print(f"{first_number} + {second_number} = {first_number + second_number}")
    else:
        print(f"{first_number} is not digit or letter")
elif operation == '-':
    print('Substraction is not developed yet')
else:
    print('Not valid operation')

