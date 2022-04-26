#
# own_range(start, end, step)

# range(10)   start=0 end=10 step=1


def own_range(start=0, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if end < start and step > 0:
        return None

    if end > start and step < 0:
        return None

    # if end > start:
    #     while start < end:
    #         yield start
    #         start += step
    #
    # elif end < start:
    #     while start > end:
    #         yield start
    #         start += step

    while start != end:  range(0, 11, 2)
        yield start
        if start + (end % step) == end:
            return
        start += step


x = own_range(0, -11, -5)
for i in x:
    print(i)
# own_range(10, -10, 1)
