# Decorators

# def decorator_function(original_function):
#     def wrapper_func(*args, **kwargs):
#         print(f'wrapper_func() executed this before {original_function.__name__}')
#         return original_function(*args, **kwargs)
#     return wrapper_func
#
# @decorator_function   # display = decorator_function(display)
# def display_info(name, age):   # wrapper_func
#     print(f'display_info executed with args: {name}, {age}')
#
# display_info('Petryk', '11')

# decorated_display = decorator_function(display)  # == wrapper_func
# decorated_display()    # == wrapper_func()
####################################################################################
from functools import wraps


def my_logger(original_func):
    import logging
    logging.basicConfig(filename=f'{original_func.__name__}.log', level=logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Function: {original_func.__name__}. Ran with args: {args} and kwargs: {kwargs}')
        return original_func(*args, **kwargs)
    return wrapper


def my_timer(original_func):
    import time

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        time.sleep(2)
        t2 = time.time()
        print(f'{original_func.__name__} executed in {t2 - t1} sec')
        return result
    return wrapper


@my_logger   #display_info = my_logger(my_timer(display_info))
@my_timer  # display_info = my_timer(display_info)
def display_info(name, age):   # wrapper_func
    return f'display_info executed with args: {name}, {age}'

print(display_info('User2', '23'))
