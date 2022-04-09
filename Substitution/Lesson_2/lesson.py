#Python 2
pattern_1 = 'Pattern text: {}, {}, {}'
print(pattern_1.format(1, 2, 3))

print('Pattern text: {0}, {0}, {0}, {0}, {1}, {1}, {1}, {0}'.format(1, 3))

pattern_2 = 'Pattern text: {first}, {last}, {age}'
print(pattern_2.format(first='Name', last='Surname', age=33))

#Python 3
name = 'nlajwndawd'
print(f'{name}')
#
# name = input('What\'s your name?')

# print('{:_<20}'.format('test'))
# print('{:_^20}'.format('test'))
# print('{0:_>20}|{0:*<10}'.format('test', 'hi'))

print()
print(0 > 1)
print(0 < 1)
print(2 == 2)
print(1 != 1)  #False
print(2 == 2.0)
print(10 > 5 > 3 < 30)
operation = (4 >= 4)
print(type(operation))
print()
print(5 >= 5)
print(5 > 5)
print()
# True/False
print(True == 1)
print(False == 0)

#is
print()
print('hello' == 'hello')

print()
x = 100000**10000
y = 100000**10000
print(x is y)
print(x == y)
print(id(x))
print(id(y))

print()
message = "hi I love you 3000!!"
message_2 = 'aaaaaaaaaaaaa'
print(message.index('o'))
print(message.lower())
print(message.upper())
print(message_2.capitalize())
print(message.center(22, '_'))
print(message.find("you"))
print(message.count('0'))
print(len(message))
print(message_2.replace('a', 'b'))
print(dir(message))
