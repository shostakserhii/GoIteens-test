class Person:
    def __init__(self, first, last):
        print('Person.__init__() ->')
        self.first = first
        self.last = last
        print('Person.__init__() <-')


class Covid5GPerson(Person):
    def __init__(self, first, last, chip, bat_dna):
        print('Covid5GPerson.__init__() ->')
        super().__init__(first, last)
        self.chip = chip
        self.bat_dna = bat_dna
        print('Covid5GPerson.__init__() <-')


class FullnamePerson(Person):
    def __init__(self, first, last):
        print('FullnamePerson.__init__() ->')
        super().__init__(first, last)
        self.fullname = f'{self.first} {self.last}'
        print('FullnamePerson.__init__() <-')


class AbbrevPerson(Person):
    def __init__(self, first, last):
        print('AbbrevPerson.__init__() ->')
        super().__init__(first, last)
        self.abbrev = f'{self.first[0]} {self.last[0]}'
        print('AbbrevPerson.__init__() <-')


class RealPerson(Covid5GPerson, AbbrevPerson):
    def __init__(self, first, last,  chip, bat_dna):
        print('RealPerson.__init__() ->')
        super().__init__(first, last,  chip, bat_dna)
        print('RealPerson.__init__() <-')


print(RealPerson.mro())
real_person = RealPerson('Baby', 'Groggo', 'GPS656', 'B52-2')
print('--------------------')
print(real_person.first)
print(real_person.last)
print(real_person.abbrev)
