#Iterable - smth that can be looped over with __iter__()

# Iterator - smth that has __next__()

nums = [1, 2, 3]

# for num in nums:
#     print(num)
#
# print(dir(nums))
#
# print(next(nums))
##########################
i_nums = nums.__iter__()  # iter(nums)   -transform list into iterator
print(i_nums)
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print()
##########################

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)
print(nums)
# for num in nums:
#     print(num)

print(next(nums))

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

####################################################


def in_range(start, end=None, step=1):
    if end == None:
        end = start
        start = 0
    if (start > end and step > 0):
        return []
    if (start < end and step < 0):
        return []

    while start != end:
        yield start
        start += step
####################################################


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

#Class vs Generator
# def sentence(sentence):
#     for word in sentence.split():
#         yield word

my_sentence = Sentence('This is a test sentence')

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))

# for i in my_sentence:
#     print(i)

##############################################################
class Person:
    def __init__(self, name, phone):
        self.name = name
        if type(phone) != str or not phone.isdigit():
            raise ValueError(f'{phone} should contains numbers only')
        self.phone = phone

    def __str__(self):
        return f'{self.name}: {self.phone}'


class PhoneBook:
    def __init__(self, *args):
        if any(not isinstance(person, Person) for person in args):
            raise ValueError
        self.ppl = args
        # self.index = 0

    def __iter__(self):
        # self.index = 0
        return iter(self.ppl)

    # def __next__(self):
    #     person = self.ppl[self.index]
    #     self.index += 1
    #     return person


person_1 = Person('gusion', '123123123123')
person_2 = Person('gossen', '123000000003')

phonebook = PhoneBook(person_1, person_2)
for person in phonebook:
    print(person)
