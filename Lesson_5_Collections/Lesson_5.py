
welcome = "helloooo!!!! wooooorld"
index = 0

while index != len(welcome):
    if welcome[index] == "o":
        index += 1
        continue
    elif welcome[index] == " ":
        break
    print(welcome[index])
    index += 1

print("HEY THERE")

number = 1
while True:
    if number % 2 != 0:
        number += 1
        continue
    print(number)
    number += 1
    if number == 1128275:
        break

str_collection = "string"

list_collection = ['string', 'tor', 'radius', 'indengt', 'ndawd', 'gawdawd']
print(len(list_collection))
print(list_collection[1:2])

new_list_collection = ["string", 123, 2.3, True, None]
print(new_list_collection)


# str_collection[0] = "a" #immutable незмінюваний тип даних: TypeError str doesn't support item assignment
new_list_collection[0] = 1234
print(new_list_collection)
print(len(new_list_collection))

# new_list_collection[11] = "11"
list_1 = [1, 2, None, '34']
list_2 = list_1
list_2[0] = '1234'

print(id(list_1))
print(id(list_2))
print(list_1, list_2)
print("===============")
a = "Hello"
print(id(a))
a = a[:3]
print(id(a))
print()
b = [1, 2, 3, 4]
print(id(b))
b[1] = "pokemon"
print(id(b))

list_collection = ['123', 4235, True, None, "dawdaefrf"]

new_collection = list_collection + [1, 3, 4]
print(new_collection)

list_collection.extend(["a", "a", "a", "a", "a", "a", "a", "a", "a"])
print(list_collection)

index = 0
while True:
    if index == len(list_collection):
        break
    if type(list_collection[index]) == str:
        index += 1
        continue
    print(type(list_collection[index]))
    index += 1

immutable_collection = ([1, 2, 3], 4235, True, None, "asasasas")
print(immutable_collection)
print(type(immutable_collection))
print(immutable_collection[3])
# immutable_collection[0] = 123 'tuple' object does not support item assignment

nested_list = [[1, 2, 3], [5, 6, 7]]
print(nested_list[1][1])
immutable_collection = ([1, 2, 3], 4235, True, None, "asasasas")
immutable_collection[0].append("hello")
print(immutable_collection)

string = "hello"
string_methods = dir(string)
print(string_methods)
