
f = open('test.txt', 'a')

def fib():
    num = 1
    next_num = 1
    while True:
        yield num
        f.write(str(num))
        num, next_num = next_num, num+next_num

fib = fib()
while True:
    print(next(fib))
