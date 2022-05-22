from First_module import first_mod_print, Taras, list_of_nums, square_nums
# import First_module
# from First_module import abracadabra
# from First_module import abracadabra as first_mod_print
from Folder_1.folder_1 import folder_1
from Folder_1.Folder_2.folder_2 import folder_2
print(__name__)
first_mod_print()

def hello():
    pass

print(hello.__name__)
print(list_of_nums)
a = Taras()
print(a)
square_nums(4)
folder_1()
folder_2()
