# First Class Func

def square(x):
    return x*x

# f = square(5)
# print(square)
# print(f)

f = square
print(square)
print(f)
print(f(5))
#######################################################################################

def my_map(func, list_of_nums):
    result = []
    for number in list_of_nums:
        result.append(func(number))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)


def cube(x):
    return x * x * x

cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)
#####################    RETURN FUNCTIONS            #################################

def logger(msg):

    def log_message():
        print('Log: ', msg)

    return log_message

log_hello = logger('Hello')
log_hello()
print(log_hello)
##############################################################

def visualize_text(symbols):

    def wrap_text(msg):
        print(f'{symbols}{msg}{symbols}')

    return wrap_text

star_text = visualize_text('***')
star_text('hello')
print(star_text('alloha')) # question to children: why is there None printed as well?