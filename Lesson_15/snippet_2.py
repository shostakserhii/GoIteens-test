# class Student:
#     university_name = 'Hogwarts'
#
#     def __init__(self, first, last, grant):
#         self.first = first  # can be whatever e.g. self.first_name
#         self.last = last
#         self.grant = grant
#         self.email = first + '.' + '@university.com'
#
#     def fullname(self):
#         return f"{self.first} {self.last}"
#
#     def decrease_grant(self):
#         self.grant = float(self.grant - 0.1)
#
# std_1 = Student('John', "Wik", 1)
# print(std_1.fullname())
# std_1.decrease_grant()
# print(std_1.grant)
# -------------------------------------------------------------------------------------------------------------------------------
# class Student:
#
#     decrease_amount = 0.1
#
#     def __init__(self, first, last, grant):
#         self.first = first  # can be whatever e.g. self.first_name
#         self.last = last
#         self.grant = grant
#         self.email = first + '.' + '@university.com'
#
#     def fullname(self):
#         return f"{self.first} {self.last}"
#
#     def decrease_grant(self):
#         self.grant = float(self.grant - decrease_amount) # -->> Student.decrease_amount | self.decrease_amount -later we will see the difference
#
# std_1 = Student('John', "Wik", 1)
# std_2 = Student('First', "Last", 0.9)
# print(std_1.fullname())
# std_1.decrease_grant()
# print(std_1.grant)
#
# #Check namespace
# print(std_1.__dict__)
# print(Student.__dict__)  #--> std_1 doesnt have decrease_amount attr, it inherits it from the Class
#
#
# #Student.decrease_amount VS Student.decrease_amount
# print(Student.decrease_amount)
# print(std_1.decrease_amount)
# print(std_2.decrease_amount)
# #--->
# std_1.decrease_amount = 0.5
# print(std_1.__dict__)
# print(std_1.decrease_amount)
# print(Student.decrease_amount)
# print(std_2.decrease_amount)
#-------------------------------------------------------------------------------------------------------------------------------

# class Student:
#
#     decrease_amount = 0.1
#     num_of_students = 0
#
#     def __init__(self, first, last, grant):
#         self.first = first  # can be whatever e.g. self.first_name
#         self.last = last
#         self.grant = grant
#         self.email = first + '.' + '@university.com'
#
#         Student.num_of_students += 1
#
#     def fullname(self):
#         return f"{self.first} {self.last}"
#
#     def decrease_grant(self):
#         self.grant = float(self.grant - self.decrease_amount) # -->> Student.decrease_amount | self.decrease_amount -later we will see the difference
#
#
# std_1 = Student('John', "Wik", 1)
# std_2 = Student('First', "Last", 0.9)
# print(Student.num_of_students)