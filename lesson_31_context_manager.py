import os
from contextlib import contextmanager


@contextmanager
def directory_elements(folder_name):
    cwd = os.getcwd()
    os.chdir(folder_name)
    yield
    os.chdir(cwd)


with directory_elements('Lesson_8'):
    print(os.listdir())

with directory_elements('Lesson_13'):
    print(os.listdir())


new_l = [1, 3]
from pprint import pprint
pprint(dir(new_l))
