# First Class Functions

def square(x):
    return x * x
#
# f = square
# print(square)
# print(f)
# print(f(5))
# print(square(5))
# print(square is f)
#

def cube(x):
    return x * x * x

def my_map(function, list_of_numbers):
    result = []
    for number in list_of_numbers:
        result.append(function(number))    #result.append(square(i))
    return result

list_of_squares = my_map(square, [1, 2, 3, 4, 5])
print(list_of_squares)

list_of_cubes = my_map(cube, [1, 2, 3, 4, 5])
print(list_of_cubes)
print('----------------------------------')
###############################################################

def logger(msg):

    def log_msg():
        print("Log: ", msg)

    return log_msg

log_hello = logger('Hello!')
print(log_hello)
log_hello()
log_bye = logger('Bye!')
log_bye()
###############################################################

def visualize_text(symbol):

    def wrap_message(msg):
        print(f'{symbol}{msg}{symbol}')

    return wrap_message

star_text = visualize_text('***')
star_text('hello')
print(star_text('bye'))
################################################################
print('---------------------')
print()
def outer_func():
    message = "Доброго вечора! МИ З УКРАЇНИ!"

    def inner_func():
        print(message)

    return inner_func

my_func = outer_func()
print(my_func.__name__)
my_func()
my_func()
my_func()
#########################################################################
