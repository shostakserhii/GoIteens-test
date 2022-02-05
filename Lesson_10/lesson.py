

students_dict = {
    'Anna': {
        'age': 15,
        'sex': 'female',
        'school': 'School #13'
    },
    'Makar': {
        'age': 14,
        'sex': 'male',
        'school': 'School #5',
        'additional courses': 'English'
    },
    'Sashko': {
        'age': 13,
        'sex': 'male',
        'school': 'School #5',
        'additional courses': 'IT'
    },
}

print(len(students_dict))   #key:value

for student, student_info in students_dict.items():
    print(f" {student}:{student_info}")



element_to_find = input("Enter value or key you want to search for: ")

list_1 = [1, 2, 3, 5, None, False]
print(1 in list_1)
print('Makar4ik' in students_dict)


element_to_find = 'male'
for student, student_info in students_dict.items():             # Ітеруємось по студентах student, student_info
    student_info_list = list(student_info.items())
    for info_element in student_info_list:
        if element_to_find in info_element:
            print(f"{element_to_find} was found in \n{student}:{student_info}")


    print(element_to_find in list(student_info.items()))

password = input('Password: ')
#         - мінімум 8 символів
#         - велика буква
#         - маленька буква
#         - цифра
#         - символ

minimum_numbers = False

if len(password) > 8:
    minimum_numbers = True

if minimum_numbers and upper_letter and digit and symbol and lower_letter:
    print(password)

list_1 = [1, 2, 3, 4, 5]

operations = ["+", "-", "q"]
print("Hello. Welcome to Calcul")
while True:
    op = input("Enter operation or 'q' to quit: ")
    if op == "q":
        print("Exiting")
        break
    else:
        print(op)

for x in list1:
    for y in list2:
        pass

for x in list1:
    if x in list2:
        pass