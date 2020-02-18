from math import factorial


def factorial_generator():
    for i in range(1, 16):
        yield factorial(i)


gen_list = factorial_generator()

for num in gen_list:
    print(num)
