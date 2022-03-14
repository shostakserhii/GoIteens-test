"""Working with files."""
read_file = open('README.md')
read_file.write('adwdawdawd')
tell()   VS     seek()
print(read_file.read(10))
print(read_file.tell())
read_file.seek(0)
print(read_file.read(15))
print(read_file.tell())  #15
read_file.seek(5)
print(read_file.read(15))
print(read_file.tell()) #20
read_file.seek(30)      #30
print(read_file.read(15))
dir(read_file)
print(type(read_file))
###############################################################################
readline()
read_file.seek(0)
print(f'the first line: {read_file.readline()}')
print(read_file.tell())
print(f'the second line: {read_file.readline()}')
print(read_file.tell())
print(f'the third line: {read_file.readline()}')
print(f'the forth line: {read_file.readline()}')
print(read_file.tell())
###############################################################################
read_file.seek(0)
print(read_file.readlines())


WRITE TO FILE
new_file = open('new_file', 'w+')
print(new_file.tell())
new_file.write('aaaaaaaaaaaaaaaa')
new_file.seek(0)
print(new_file.read(10))
new_file.close()

#APPENDING TO FILE
new_file = open('new_file', 'a+')
print(new_file.tell())
new_file.write('oajwhdouahwd\n')
print(new_file.tell())
print(new_file.read(10))
new_file.close()

###############################################################################
JSON

json_like = [
    {
    'name': 'Bob',
    'magazines': ['check', 2, 'bath']
    },
    {
    'name': 'Anna',
    'magazines': ['Natali', 'Lito2020', 'Garden']
    }
]
lookup_map1 = [{
    'Bob': ['check', 'math', 'bath'],
    'Anna': ['Natali', 'Lito2020', 'Garden']
}]
lookup_map2 = {
    'Bob': {
        'magazines': ['check', 'math', 'bath']
    },
    'Anna': {
        'magazines': ['Natali', 'Lito2020', 'Garden']
    }
}
import json
json_file = open('new.json', 'w')
print('simple print')
print(json_like)
print('json print')
print(json.dumps(json_like, indent=4))    # DUMPS   - приймає стрічку
json.dump(json_like, json_file, indent=4)
json_file.close()

#READ JSON
json_file2 = open('new.json', 'r')
print('simple print')                                               #1234
json_content = (''.join([i for i in json_file2]))
print('json print')
json_file2.seek(0)
json_load = json.load(json_file2)   # waiting for FILE
print(type(json_load))
print(json_load)

json_obj = json.loads(json_content)   # waiting for STR
print(type(json_obj))
print(json_obj)

import datetime
def logging(a, b):
    memory.json
    [{
        'login':'',
        'password':'',
    }]
    pass
