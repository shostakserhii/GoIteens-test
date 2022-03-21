# print(10 / 0)

# dict_ex = {}
# dict_ex['key']

# int('nine')


# def div(x, y):
#     if y == 0:
#         raise ZeroDivisionError
#     return x / y
#
#
# print(div(1, 2))
#
# try:
#     print(div(1, 0))  # <-- ZeroDivisionError
#     print(div(1, 2))
#     print('if try -block succeed')
# except ZeroDivisionError:
#     print('ай айайй не можна ділити на 0!!!!')
# finally:
#     print('finally')

dict = {
    'first': 1,
    'second': 2
}

# def get_key(dict, key):
#     if key not in dict:
#         raise KeyError(key)
#     return dict[key]


# print(get_key(dict, 'first'))
# print(get_key(dict, 'third'))


# try:
#     print(dict['third'])   #KeyError
#     print('if try -block succeed')
# except ZeroDivisionError:
#     print('ай айайй не можна ділити на 0!!!!')
# except KeyError as e:
#     print(e)
# finally:
#     print('finally')


# a = ['1', '33', '43', '123', 'a', 45, 'b', '12', 'c']
#
# digits = []
# failed_results = []
# i = 0
# while i < len(a):
#     try:
#         int(a[i])
#         digits.append(a[i])
#     except ValueError:
#         failed_results.append(a[i])
#     finally:
#         i += 1
#
# print(digits)
# print(failed_results)

import json

json_like_dict = [
    {
    'name': 'a',
    'surname': 'b'
    },
    {
    'name': 'cc',
    'surname': 'dd'
    }
]

# json_file = open('new.json', 'w')
# json.dump(json_like_dict, json_file, indent=4)


try:
    json_file_read = open('new.json')
    data = json.load(json_file_read)
    print(data)
except FileNotFoundError:
    print('No file, sorry')
    data = []
except json.decoder.JSONDecodeError as e:
    print(e)
    data = []
finally:
    print(data)
    print('no worries, even if there is problem I will handle it')
