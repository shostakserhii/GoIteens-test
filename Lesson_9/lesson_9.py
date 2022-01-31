import random
import math

#Dictionary
#
# empty_dict1 = {}
# empty_dict2 = dict()
#
#
# not_empty_dict1 = {
#     'key1': 1,
#     'key2': False,
#     'key3': 'string',
#     'key4': [1, 2, 3],
#     'key5': -5
# }
#
# # print(not_empty_dict1['key1'])
# # print(not_empty_dict1['key2'])
# # print(not_empty_dict1['key3'])
# # print(not_empty_dict1['key4'])
# # print(not_empty_dict1['key5'])
#
# list_comp = [number for number in range(11)]
# print(list_comp)
#
# dict_comp = {index: value for index, value in enumerate(range(1, 11))}
# print(dict_comp)
#
# dict_comp['name'] = 'Iron man'
# dict_comp['name2'] = True
# dict_comp['our first dict'] = not_empty_dict1
# print(dict_comp)
#
# print(type(dict_comp.keys()))
# print(list(dict_comp.keys()))
# print(list(dict_comp.values()))
# print(dict_comp.items())
#
# print(dict_comp)
# print(list(dict_comp.items()))
#
# for value in dict_comp.items():
#     print(value)
#
# heroes_by_universe = {}
# # print(heroes_by_universe)
# heroes_by_universe['DC'] = ['Batman', 'Flash', 'Superman', 'Aqua Man']
# # print(heroes_by_universe)
# heroes_by_universe['Marvel'] = ['Iron Man', 'Wonder Woman', 'Spider Man']
# # print(heroes_by_universe)
#
# # operations = {}
# # operations['print'] = print
# # func = operations['print']
# # func("hello world")
#
# for universe_with_heroes in heroes_by_universe.items():
#     print(universe_with_heroes)
#
# print(list(heroes_by_universe))
#
# operations = {
#     'add': '',
#     'sub': '-',
#     'div': '/',
#     'mul': '*'
# }

# numbers = [2, 3]
#
# print(sum(numbers))
# print()
# operation = input("Name operation!  ")

# if operation in operations:
#     print(operations[operation])
# else:
#     print(f'{operation} is not supported')

print()
student_Jade = {'name': 'Jane', 'age': 23, 'sex': 'female'}
print(student_Jade)
print(student_Jade.get('phone', 'Sorry, not Found'))

# students['phone'] = '444-444-5555'
# students['address'] = 'Kyiv, Khreshchatyk'
# students['name'] = 'Jade'

student_Jade.update({'name': 'Jade', 'address': 'Kyiv, Khreshchatyk', 'phone': '444-444-5555'})
student_Mark = {
    'name': 'Mark',
    'age': 30,
    'courses': ['Math', 'Eng', 'CompSience']
}

students_all = {
    'Jade': student_Jade,
    'Mark': student_Mark
}

print(students_all['Mark']['courses'])

# DEL vs POP
print(student_Jade)
# del student_Jade['phone']
jades_number = student_Jade.pop('phone')
print(student_Mark)
student_Mark['number'] = jades_number
print(student_Mark)


first_number = 2
second_number = 3
op = input('Operation: ')
if op == '+':
    print(first_number + second_number)


