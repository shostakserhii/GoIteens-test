#Closures
def outer_func():
    message = 'Hi!'

    def inner_func():
        print(message)

    return inner_func

my_func = outer_func()
print(my_func.__name__)
my_func()
my_func()
my_func()

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func('Слава Україні!')
hi_in_return = outer_func('Героям слава!')
hi_func()
hi_in_return()