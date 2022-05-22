def get_sqr(number_list):
    for item in number_list:
        if type(item) != int and type(item) != float:
            raise ValueError
    result_list = []
    for item in number_list:
        result_list.append(item**2)
    return result_list

example = [1,2,3,4]
print(get_sqr(example))

def get_sqr_2(number_list):
    if any(type(item) != int and type(item) != float for item in number_list):
        raise ValueError
    result_list = [item**2 for item in number_list]
    return result_list


def own_any(iterable):
    for item in iterable:
        print(item)
        if item == True: # VS if item:
            return

own_any((False, False, True, False))
own_any([False, False, '123', '456'])
own_any(['', [], {}, 0, '123', ''])
#########################################################

# with open('test', 'w') as f:
#     for i in range(10000000):
#         print(i)
#         f.write(str(i)+'\n')

# with open('test', 'r') as f:
#     items = f.read()
# print(items)



def read_file():
    f = open('test')
    for line in f:
        yield line

file_data = read_file()
print(file_data)
print(next(file_data))
print(next(file_data))
print(next(file_data))

#######################################################
def fib():
    num = 1
    next_num = 1
    while True:
        yield num
        num, next_num = next_num, num + next_num