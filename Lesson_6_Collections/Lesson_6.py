Collections

str   Immutable
list  Mutable
tuple Immutable

single = [1]
print(type(single))
single_t = (1)
print(type(single_t))

a, b, c = "123"
print(a)
print(b)
print(c)

a = 1,
print(type(a))
print(len(a))

a = 1, None, False, "str", (1, 2, 3)
print(type(a[-1]))

l = [1, 2, 3]
print(l)
l2 = [4, 5, 6]
l.extend(l2)
print(l)
print(len(l))

l.append(l2)
print(l)
print(len(l))
print(l)

a = ["hello", "world", "I", "am", "back"]
print(a)

removed_value = a.pop(1)
print(removed_value)

del a[1]
print(a)

a = [0]
print(type(a))

a, = [1]
print(type(a))


#String
string_1 = 'dasdawd' or "dawdawd"
string_2 = """
dhaouwhdawd
"""
string_3 = str(1234)

a, b, c = ["one", "two"]

index()
print("hello world".index('wor'))

numbers = "   10.5        +            333       "

numbers_2 = numbers.strip().split().count('333')
print(numbers.strip().split())
print(numbers_2)

print(type(numbers.split()))
first_number, second_number = numbers.strip().split('+')
print(first_number)
print(second_number)

word = "hello"
if 'l' in word:
    print("yes")


add = '+'
sub = '-'
div = '/'
множення = '*'

allowed_operations = [add, sub, div, множення]
user_operation = input("Enter operation: ")
if user_operation in allowed_operations:
    print('Good')
else:
    print(f"{user_operation} is not supported yet")

кортеж = 1, 2, 3
print(type(кортеж))
список = list(кортеж)
print(список)
кортеж_2 = tuple(список)
print(кортеж_2)

print(float(1))
print(int(1.2))

print(tuple("123412342"))
print(list("123412342"))
print(type)
print(str(tuple("123412342")))

tupler = list("123412342")
print(tupler)
print(''.join(tupler))

add = '+'
sub = '-'
div = '/'
mul = '*'

supported_operations = [add, sub, div, mul]

print(f"""
Choose operations from list:
{', '.join(supported_operations)}
""")

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 3]
append()
extend()
pop()
l.insert(1, 1123123123)
print(l)

l.remove(3)
print(l)

