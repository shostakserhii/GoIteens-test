# name = "xsxa"
# surname = "dawdawd"
# middle_name = "dawdaczdczdf"
# print(f"""
# name: {name}
# surname: {surname}
# middle name:{middle_name}
# """)
# print(True and True) #True
# print(True or False) #True
# print(False or True) #True
# print(False and True) #False
# print()
# print(False or 0 or bool(0) or 0 or False)
#
# print(not(1 == 1))
# x = 10
# x = x is None and input("x: ")
# x = x is not None or input("x: ")
# print(x)
#
# x = False or 0 or '' or None or 0
# print(x)

# x = 100
#
# if x == 100:
#     print("x == 100")
#     if x > 150:
#         print(x > 50)
#     elif x > 90:
#         print("x > 90")
#     elif x > 60:
#         print(x > 60)
#     else:
#         print("Fake")
# elif x > 0:
#     print("x > 0")
# elif x < 200:
#     print("x < 200")
# elif x > 100:
#     print("x > 100")
# else:
#     print("else x > 100")


# x = int(input("x: "))
# start = 0
#
# while start <= x:
#     print(start)
#     start += 1

# x = int(input("x: "))
#
# index = 1
# factorial = 1
#
# while index <= x: # x = 5
#     factorial = factorial * index   # 120 = 24 * 5
#     print(f"factorial: {factorial}, index: {index}")
#     index += 1
#     #index = 6


# string = "abcdefg"
#
# while string:   #while "": --> False
#     string = string[:-1]      # abcdefg  --->   abcdef
#     print(string)


# number = 20
# start = 0
#
# while start < number:
#     print(start)
#     if start == 10:
#         break
#     start += 1
#
# print(f"finish: {start}")

welcome = "helloooo wooooorld"
index = 0
print(len(welcome))

while index != len(welcome):
    if welcome[index] == "o":
        index += 1
        continue
    index += 1
    print(welcome[index])

