#
def hello():
    print('Hello!')


def validate_user_input(user_input):
    if user_input.isdigit():
        return user_input
    else:
        return "Not a digit"


number = input("Enter number: ")    #10
result = validate_user_input(number)
print(f"result: {result}")

print(len("hello"))

def hello_func(name, last_name, greeting='Hello', bye_word='Bye'):    #Positional arguments: name, last_name
    return f"        {greeting}, {name} {last_name}! {bye_word}         "              #Keyword arguments:    greeting

result = hello_func('ivy', 'handleson', bye_word='ari viderchi!', greeting='salut').strip().capitalize()
print(result)
def hello(first, *, second=None, third='asdawdawd', forth='4444444'):
    print(first)
    print(second)
    print(third)
    print(forth)

hello(1, second=2, third=3, forth=4)
print()

def input_digits():
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    return first, second


def division_with_check(first, second):
    result = float(first) / float(second)
    if result.is_integer():
        return int(result)
    else:
        return result


def check_if_float_or_int(number):
    number = float(number)
    if number.is_integer():
        return int(number)
    return number



first_number, second_number = input_digits()
division_with_check(first_number, second_number)


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math', 'itSci', name='Angelina', age='33', dawd ='dawdawdawd' )

courses = ['math', 'itSci']
student = {'name': 'Angelina', 'age': '33', 'dawd': 'dawdawdawd'}

student_info(courses, student)

def packing_values(*args):
    print(*args)

packing_values(1, 2, 3, 4, None)

def unpacking_values(a, b, c):
    print(a)
    print(b)
    print(c)

unpacking_values(*[1, 2, 3])

