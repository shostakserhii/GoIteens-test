"""Code Style/ Style Guide
Mainly Pep8

IMPORTS:
1 standard library modules

2 downloaded modules

3 local modules
"""
import glob
import os

import dataclasses

import Test_2022
import Lesson_8


# hello
def func(item=None):  # hello
    """
    Snake case.
    Before and after function 2 blank lines.
    Comment before function with 1 space or from right side with 2 spaces
    Docstring inside function with double quotes
    """
    return item


class Sample:
    """
    Camel case
    Before and after Class 2 blank lines
    One blank line between methods.
    """
    def __init__(self):
        pass

    def smth(self):
        print('hello')


# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# flake8


item = 2  # Operators should all be separated with spaces except for assigned operator in function
from typing import Dict, List, Iterable, Iterator, Union, Optional, Any
"""TYPE HINTING
MYPY
"""
"""It happens that you rewrite variables somewhere. e.g."""
x = 1
y = 2
x = '3'
y = '4'
"""let's try another way"""
x = input('X: ')
y = input('Y: ')


def add(num_1: int, num_2: int) -> int:
    """Comment"""
    return sum([num_1, num_2])

# def div(num_1: Union[int, float], num_2: Union[int, float]) -> Union[int, float]:
def div(num_1: int, num_2: int) -> float:
    """Comment"""
    result = num_1 / num_2
    if type(result) == float and result.is_integer():
        return int(result)
    return result


print(add(x, y))
div(10.2, 2)


def equal(item1: Any, item2: Any) -> bool:
    """Equal comment"""
    return item1 == item2

# def format(data: str, separator: Optional[str] = None) -> Union[Optional[str], List[str]]:
def format(data: str) -> str:
    # if separator is not None:
    #     return data.strip().split(separator)
    if data.isalpha():
        return data.strip()   # поверне нічого VS нічого не поверне
    return None

print(equal(1, '1'))

StrToStrDict = Dict[str, str]
Phonebook: StrToStrDict = {'123': 'abc'}
CellPhone: StrToStrDict = {'+24234': 'Gosha'}

# pip install mypy
# pip install flake8
# flake8 file.py - for style check
# mypy file.py - type hint