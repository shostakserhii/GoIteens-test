#Decorators

# def decorator_function(msg):
#     def wrapper_function():
#         print(msg)
#     return wrapper_function
#
# hi_func = decorator_function('HI!')
# bye_func = decorator_function('BYE!')
#
# hi_func()
# bye_func()
#########################################

def decorator_function(original_func):
    def wrapper_function():
        print(f'wrapper executed this before {original_func.__name__}')
        return original_func()
    return wrapper_function

#@decorator_function ==  #display = decorator_function(display)
def display():
    print('display() executed')

decorated_display = decorator_function(display)
decorated_display()

#####################################################################################
def decorator_function(original_func):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_func.__name__}')
        return original_func(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_info(name, age):
    print(f'display_info ran with args: {name}, {age}')

display_info('Petryk', '12')
######################################################################################
#
# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print(f'__call__ method ran this before {self.original_function}')
#         return self.original_function(*args, **kwargs)
###########################################################################################
from functools import wraps
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(original_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        time.sleep(2)
        t2 = time.time()
        print(f'{original_func.__name__} ran in: {t2-t1} sec')
        return result
    return wrapper


@my_timer   #display_info = my_timer(decorator_function(display_info))
@my_logger     #display_info = decorator_function(display_info)
def display_info(name, age):
    print(f'display_info ran with args: {name}, {age}')

display_info('Petryk', '12')

