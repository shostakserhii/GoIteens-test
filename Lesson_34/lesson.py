"""
Code Style / Style Guide
PEP8

Required packages:
pip install flake8
pip install mypy


Run:
flake8 file.py
mypy file.py
"""
import os
import sys
import random
from typing import Dict, List, Any, Optional, Iterator, Iterable, Union

import dataclasses  # pip install dataclasses

# from Test_2022.test_2022 import power_3


# comment
def return_value(value=None):  # i named return value cause I liked it
    """
    Snake case
    Before and after func should be 2 blank lines
    Docstring should be with 3 double quotes inside function
    """
    return value


class Sample:
    """
    Camel Case
    Before and after class should be 2 blank lines
    One blank line between methods
    """
    def __init__(self):
        pass

    def some_method(self):
        pass


item = 2

"""TYPE HINTING
mypy
"""


def add(num_1: int, num_2: int) -> int:
    """Comment"""
    return num_1 + num_2


def div(num_1: Union[int, float], num_2: Union[int, float]) -> \
        Union[int, float]:
    """Comment"""
    result = num_1 / num_2
    if type(result) == float and result.is_integer():
        return int(result)
    return result


x = 1
y = 3
# x = '1'
# y = '3'

print(add(x, y))
print(div(4.4, 2.1))


def equal(item_1: Any, item_2: Any) -> bool:
    """Comment"""
    return item_1 == item_2


def formatter(data: str, separator: Optional[str] = None) -> \
        Union[Optional[str], List[str]]:
    """Comment"""
    if separator:
        return data.split(separator)
    if data.isalpha():
        return data.strip()  # поверне ніщо VS нічого не поверне
    return None


formatter('hello hello')


DictWithTwoStr = Dict[str, str]
Phonebook: DictWithTwoStr = {'123': 'abc'}
Phone: DictWithTwoStr = {'Styopa': '+3494534'}
