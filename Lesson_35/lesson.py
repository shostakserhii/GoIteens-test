def factorial(n):
    """5!  =  5 * 4 * 3 * 2 * 1."""
    if n == 1:
        return n
    return n * factorial(n - 1)


def fibonacci(n: int, x=0, y=1):        #6
    """0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    x   y
    0   1
    1   2
    2   3
    3   5
    5   8
    """
    x = 0
    y = 1
    for i in range(n):
        x, y = y, x + y
    print(x)


def recursive_fib(n: int, x=0, y=1):  # n = 0 x = 21 y = 44
    if n == 0:
        print(x)
        print(y)
        return x, y
    print(x)
    recursive_fib(n-1, y, x + y)




def polindrom():
    pass


def print_reverse(our_list: list):  # [1, 2, 3, 4, 5]  [1, 2, 3, 4] [1, 2, 3]   [1, 2]   [1]   []
    if not our_list:
        return
    print(our_list.pop())  # 5   4   3    2    1
    print_reverse(our_list)  # [1, 2, 3, 4]   [1, 2, 3]    [1, 2]   [1]   []


print_reverse([1, 2, 3, 4, 5])
print(factorial(5))
fibonacci(8)
recursive_fib(8)
