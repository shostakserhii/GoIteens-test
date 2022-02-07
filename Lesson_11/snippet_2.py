def hello_func():
    print("Hello there! ")


def hello_func():
    return("Hello there! ")


print(len('test')) #we dont know what is happening inside len - we just get the result of 4
print(hello_func().upper())


def hello_func(greeting):
    return greeting


hello_func() # Error
hello_func('Hi')


def hello_func(greeting, name):
    return f"{greeting}, {name}!"

print(hello_func('Hi', name="Bobby"))

def hello_func(name, greeting = 'Hello'):          # Positional Arguments позиційні аргументи
                                                   # Keyword Arguments
    return f"{greeting}, {name}!"


def hello_func(name, greeting = 'Hello', second_name):
    return f"{greeting}, {name}!"


def hello(first, second= None, third = 'dawdaw'):
    print(first)
    print(second)
    print(third)

def hello(first, second= None, third = 'dawdaw'):
    print(first)
    print(second)
    print(third)

hello(1, 3)

def hello(first, *, second= None, third = 'dawdaw'):
    print(first)
    print(second)
    print(third)


# validate and convert digit to float or int

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Music', name='Ivy', age=33)
courses = ['Math', 'Music']
info = {'name': 'Ivy', 'age': 33}
student_info(courses,info)

def packs_many_values(*args):
    print(*args)

def unpack_3_values(a, b, c):
    print(a)
    print(b)
    print(c)
unpack_3_values(*[1, 2, 3])
