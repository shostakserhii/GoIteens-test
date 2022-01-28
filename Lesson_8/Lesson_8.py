import random

data_list = []
number = 0
while number < 11:
    data_list.append(number)
    number += 1
print(data_list)

index = 0
while index < len(data_list):
    print(data_list[index])
    index += 1

number = random.randint(0, 11)
print(number)

list_with_data = []
index = 0
while index < 10:
    list_with_data.append(random.randint(0, 11))
    index += 1

print(list_with_data)

# SET
l1 = [1, 2, 3, 4, 5, 1, 2]
t1 = (1, 2, 3)
s1 = {1, 2, 3, False, 'string', 2, 3, False}


fruit_set = {"apple", "orange", "pineapple"}
fruit_set.add("mellon")
print(fruit_set)

x = {'a', 'b', 'c', 'e'}
y = {'c', 'd', 'e'}
z = {'g', 'h', 'c', 'e'}

result = x.intersection(y, z)
print(result)

set_way_1 = {1, 2, 3}
set_way_2 = set((1, 2, 3))

# remove()
# vs
# discard()

taken_item = set_way_1.pop()
print(taken_item)
if taken_item:
    print(taken_item)
    print("hello")

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0
while index < len(l1):
    print(l1[index])
    index += 1

for number in l1:
    if number % 2 == 0:
        print(number)
for tuple_1 in enumerate(l1):
    print(tuple_1)

for index, value in enumerate(l1):
    if index % 2 == 0:
        print(value)


l_range_1 = list(range(10, 21))
l_range_2 = list(range(10, 101, 5))

print(l_range_1)
print(l_range_2)

our_list = [number for number in range(0, 21) if number % 2 == 0]
print(our_list)


our_list = []
for number in range(0, 10):
    if number % 2 == 0:
       our_list.append(number)
print(our_list)

list_of_choices = random.choices(range(10, 20), k=10)
print(list_of_choices)

tuple_of_choices = tuple(list_of_choices)
print(set(tuple_of_choices))


random_list = ([random.randint(0, 100) for element in range(0, 10)])
print(random_list)

print()
print(list(range(0, 10)))

for element in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
   print(random.randint(0, 100))

index = 0
while index < 10:
    name = random.choices(['a', 'b', 'c', 'b', 'd', 'e'], k=3)
    name = ''.join(name)
    print(name)
    index += 1

list_of_names = ([random.choices(['Serhii', 'Sasha', 'Dima']) for item in range(10)])
print(list_of_names)

