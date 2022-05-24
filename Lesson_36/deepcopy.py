from copy import deepcopy

person = {
    'first': None,
    'last': None
}

person_1 = deepcopy(person)
person_1['first'] = 'Taras'
person_1['last'] = 'Ananas'

person_2 = deepcopy(person)
person_2['first'] = 'Illyiha'
person_2['last'] = '2 wuha'

person_3 = deepcopy(person)
person_3['first'] = 'Styopa'
person_3['last'] = 'Bender'

print(person_2['first'])
print(person_1['first'])
print(person_3['first'])
print(id(person))
print(id(person_1))
print(id(person_2))
print(id(person_3))
