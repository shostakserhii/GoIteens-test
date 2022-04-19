import random
import time
from sys import getsizeof

def create_10mln_records():

    results = []
    for i in range(1000000):
        person = {
            'id': i,
            'name': random.choice(['Rafik', 'Gozello', 'Petya', 'Strelok', 'Alucard']),
            'age': random.randint(1, 100)
        }
        results.append(person)

    return results


def generate_10mls_records():
    for i in range(1000000):
        person = {
            'id': i,
            'name': random.choice(['Rafik', 'Gozello', 'Petya', 'Strelok', 'Alucard']),
            'age': random.randint(1, 100)
        }
        yield person

# start = time.time()
# results_func = create_10mln_records()
# print(str(getsizeof(results_func)/(1024*1024)) + ' Mb')
# for i in results_func:
#     print(i)
# print(f'{time.time() - start} sec')

# print('----VS----')
t1 = time.time()
results_gen = generate_10mls_records()
print(str(getsizeof(results_gen)) + ' bytes')
# for i in results_gen:
#     print(i)
print(f'Time: {time.time()-t1} sec')
