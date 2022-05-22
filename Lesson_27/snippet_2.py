def square_num(nums):
    # results = []
    # for i in nums:
    #     results.append(i*i)
    # return results
    for i in nums:
        yield i*i

my_nums = square_num([1,2,3,4,5])
print(dir(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# print(next(my_nums))   #StopIteration
##########################################################
# my_nums = [x*x for x in [1,2,3,4,5]] - list
my_nums = (x*x for x in [1,2,3,4,5]) #- generator
print(type(my_nums))
print(my_nums)

import random
import time
from sys import getsizeof

def create_1mln_records():
    result = []
    for i in range(1000000):
        person = {
            'id': i,
            'name': random.choice(['Rafik', 'Gozelo', 'Kam', 'Lolo', 'Zorya']),
            'age': random.randint(10, 30)
        }
        result.append(person)
    return result

def generate_1mln_records():
    for i in range(1000000):
        person = {
            'id': i,
            'name': random.choice(['Rafik', 'Gozelo', 'Kam', 'Lolo', 'Zorya']),
            'age': random.randint(10, 30)
        }
        yield person


time1 = time.time()
results = generate_1mln_records()
print(str(getsizeof(results)/(1024*1024))+'Mb')   #1024*1024
print(type(results))
# for i in results:
#     print(i)
time2 = time.time()
print(f'{time2 - time1} sec')
