def add(x, y):
    """add func"""
    return int(x + y)


def subtract(x, y):
    """sub func"""
    return x - y


def multiply(x, y):
    """mul func"""
    return x * y


def divide(x, y):
    """div func"""
    if y == 0:
        raise ValueError('Cannot divide by 0')
    return x / y
