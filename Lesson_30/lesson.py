# Iterable - something that can be looped over
#__iter__()

# Iterator - smth that has __next__()
from pprint import pprint

nums = [1, 2, 3]

# for i in nums:
#     print(i)

# print(type(nums))
# print(next(nums))   #'list' object is not an iterator
# pprint(dir(nums))
# iter_nums = iter(nums)  # iter()  transform list into iterator
# print('------------------')
# pprint(dir(iter_nums))
# print(type(iter_nums))
# print(next(iter_nums))
# print(next(iter_nums))
# print(next(iter_nums))

#
# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         value = self.start
#         self.start += 1
#         return value
#
#
# def my_range(start, end):
#     while start < end:
#         yield start
#         start += 1
#
# own_range = MyRange(1, 10)
# print(type(own_range))

# for i in own_range:
#     print(i)
# for i in own_range:
#     print(i)
# print()
# for i in my_range(1, 10):
#     print(i)


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


def gen_sentence(sentence):
    for word in sentence.split():
        yield word

#
# my_sent = Sentence('This is test sentence')
# for i in my_sent:
#     print(i)
#
# for i in gen_sentence('This is test sentence'):
#     print(i)


class Person:
    def __init__(self, name, phone):
        self.name = name
        if type(phone) != str or not phone.isdigit():
            raise ValueError(f'{phone} has to contain digits!')
        self.phone = phone

    def __str__(self):
        return f'{self.name}: {self.phone}'

p1 = Person('user', '1234435')
p2 = Person('test', '3434567')

class PhoneBook:
    def __init__(self, *args):
        for i in args:
            if not isinstance(i, Person):
                ValueError
        self.contacts = args
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.contacts):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.contacts[index]


phonebook = PhoneBook(p1, p2)
for i in phonebook:
    print(i)

