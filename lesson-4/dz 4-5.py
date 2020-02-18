from functools import reduce


def my_multi(a, b):
    return a * b


print(reduce(my_multi, list(range(100, 1001))))
