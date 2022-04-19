def square_num(nums):
    for i in nums:
        yield i*i

# my_nums = square_num([1,2,3,4,5,6])
# print(my_nums)                          #[1, 4, 9, 16, 25, 36]
#
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# for i in my_nums:
#     print(i)

my_nums = (i*i for i in [1, 2, 3, 4, 5, 6])
print(type(my_nums))
print(my_nums)


for element in my_nums: #print(next(my_nums)) print(next(my_nums)) print(next(my_nums))
    if element == 9:
        print(element)
        break
    print(element)

print('---------')

for element in my_nums: #print(next(my_nums)) print(next(my_nums)) print(next(my_nums))
    print(element)

